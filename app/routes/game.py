from flask import Blueprint, session, request, current_app, redirect, url_for, flash, render_template
from app.services.game_logic import engine as GAME_ENGINE
from app.config import Config
import time
import os 
from app import db
from app.models import User, discoveredMonsters 

game_bp = Blueprint('game', __name__) 

@game_bp.context_processor
def inject_background(): 
    bg_fol = os.path.join(current_app.static_folder, 'images', 'backgrounds')
    try: 
        bg_files = [f for f in os.listdir(bg_fol) if f.endswith(('.png', '.jpg', '.jpeg'))]
    except FileNotFoundError: 
        bg_files = [] 
    return {'bg_files': bg_files}

def _start_game(difficulty):
    diff_map = current_app.config['DIFFICULTY']
    diff = difficulty if difficulty in diff_map else 'medium'
    
    forced = current_app.config.get('DEBUG_MONSTER') if current_app.config.get('CHEAT_MODE') else None
    if forced: print(f"Debug mode: Forcing monster to {forced}")

    session.update({
        'difficulty': diff,
        'total_turns': diff_map[diff],
        'guesses': [],
        'turns_taken': 0,
        'game_over': False,
        'game_status': 'playing',
        'selected_monster': GAME_ENGINE.select_monster(forced),
        'start_time': time.time(),
        'best_guess': None
    })

def _update_stats(win):
    if 'user_id' not in session: return
    user = User.query.get(session['user_id'])
    if not user: return

    discovered_monster = session.get('selected_monster')
    already_found = discoveredMonsters.query.filter_by(
        user_id=user.id, 
        monster_name=discovered_monster
    ).first()

    user.games_played += 1

    if win:
        user.games_won += 1
        user.current_streak += 1
        if not already_found:
            new_unlock = discoveredMonsters(monster_name=discovered_monster, user_id=user.id)
            db.session.add(new_unlock)
    else:
        user.games_lost += 1
        user.current_streak = 0
    db.session.commit()


@game_bp.route('/set_difficulty', methods=['POST'])
def set_difficulty():
    uid, uname = session.get('user_id'), session.get('user')
    session.clear() 
    if uid: session.update({'user_id': uid, 'user': uname})
    _start_game(request.form.get('difficulty'))
    return redirect(url_for('game.game_loop'))

@game_bp.route('/game_loop', methods=['GET', 'POST'])
def game_loop(): 
    debug_monster = current_app.config.get('DEBUG_MONSTER')
    if debug_monster and session.get('selected_monster') != debug_monster:
        _start_game(session.get('difficulty', 'medium'))

    if not session.get('selected_monster'):
        return redirect(url_for('game.default'))

    if request.method == 'POST' and not session.get('game_over'):
        guess = " ".join(request.form.get('monster_guess', '').split()).title()

        if guess and GAME_ENGINE.is_valid_guess(guess):
            guesses = session.get('guesses', [])
            if any(g['guess'] == guess for g in guesses):
                flash(f"You already guessed {guess}. Try a different monster.")
            else:
                session['turns_taken'] += 1 
                result = GAME_ENGINE.compare_guess(guess, session['selected_monster'])
                
                best = session.get('best_guess')
                if not best or result['score'] > best['score']:
                    session['best_guess'] = result
                
                guesses.insert(0, result)
                session['guesses'] = guesses
                session.modified = True 
                
                if result['is_correct']:
                    session.update({'game_over': True, 'game_status': 'win'})
                    _update_stats(True)
                    session['final_time'] = round(time.time() - session.get('start_time', time.time()), 2)
                elif session['turns_taken'] >= session['total_turns']:
                    session.update({'game_over': True, 'game_status': 'lose'})
                    _update_stats(False)
                    session['final_time'] = round(time.time() - session.get('start_time', time.time()), 2)
        elif guess:
            flash(f"{guess} is not a valid monster name. Please try again.")
        return redirect(url_for('game.game_loop'))

    img_url = url_for('static', filename=f"images/{session['selected_monster']}.png") if session.get('game_over') else None

    return render_template('game.html', 
                           guesses=session.get('guesses', []), 
                           headers=GAME_ENGINE.headers,
                           session_data=session, 
                           highlight_name=session.pop('highlight_guess', None),
                           monster_image_url=img_url)
   

@game_bp.route('/default', methods=['GET', 'POST'])
def default(): 
    if 'user' not in session: return redirect(url_for('auth.login'))
    _start_game('medium')
    return redirect(url_for('game.game_loop'))