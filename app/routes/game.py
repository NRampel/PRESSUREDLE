from flask import Blueprint, session, request, current_app, redirect, url_for, flash, render_template
from app.services.game_logic import engine as GAME_ENGINE
from app.config import Config
import time

game_bp = Blueprint('game', __name__) 

@game_bp.route('/set_difficulty', methods=['POST'])
def set_difficulty():
    session.clear() 

    difficulty_level = current_app.config['DIFFICULTY']
    chosen_difficulty = request.form.get('difficulty', 'medium')
    if chosen_difficulty not in difficulty_level:
        chosen_difficulty = 'medium' 
    session['difficulty'] = chosen_difficulty
    session['total_turns'] = difficulty_level[chosen_difficulty]
    session['guesses'] = []
    session['turns_taken'] = 0
    session['game_over'] = False
    session['game_status'] = 'playing'
    forced_name = None

    if current_app.config.get('CHEAT_MODE') and current_app.config.get('DEBUG_MONSTER'):
        forced_name = current_app.config['DEBUG_MONSTER']
        print(f"Debug mode: Forcing monster to {forced_name}")
    session['selected_monster'] = GAME_ENGINE.select_monster(forced_name) 
    session['start_time'] = time.time() 
    return redirect(url_for('game.game_loop'))

@game_bp.route('/game_loop', methods=['GET', 'POST'])
def game_loop(): 
    if not session.get('selected_monster'):
        return redirect(url_for('game.default'))
    if request.method == 'POST':
        if not session.get('game_over', False):
            user_guess = request.form.get('monster_guess', '').strip()

            if user_guess and GAME_ENGINE.is_valid_guess(user_guess):
                previous_guesses = [g['guess'] for g in session.get('guesses', [])]
                if user_guess in previous_guesses:
                    flash(f"You already guessed {user_guess}. Try a different monster.")
                else:
                    session['turns_taken'] += 1 
                    guess_result = GAME_ENGINE.compare_guess(user_guess, session['selected_monster'])
                    session['guesses'].insert(0, guess_result)
                    if guess_result['is_correct']:
                        session['game_over'] = True
                        session['game_status'] = 'win'
                    elif session['turns_taken'] >= session['total_turns']:
                        session['game_over'] = True
                        session['game_status'] = 'lose'
                    end_time = time.time() 
                    start_time = session.get('start_time', end_time)
                    session['final_time'] = round(end_time - start_time, 2)
            elif user_guess:
                flash(f"{user_guess} is not a valid monster name. Please try again.")
        session.modified = True 
        return redirect(url_for('game.game_loop'))

    highlight_name = session.pop('highlight_guess', None)  

    monster_image_url = None
    if session.get('game_over') and session.get('selected_monster'):
        monster_name = session['selected_monster']
        monster_image_url = url_for('static', filename=f'images/{monster_name}.png')

    return render_template('game.html', 
                           guesses=session.get('guesses', []), 
                           headers=GAME_ENGINE.headers,
                           session_data=session, 
                           highlight_name=highlight_name,
                           monster_image_url=monster_image_url)
   

@game_bp.route('/default', methods=['GET', 'POST'])
def default(): 
    session['difficulty'] = 'medium'
    session['total_turns'] = 9
    session['guesses'] = []
    session['turns_taken'] = 0
    session['game_over'] = False
    session['game_status'] = 'playing'
    forced_name = None

    if current_app.config.get('CHEAT_MODE') and current_app.config.get('DEBUG_MONSTER'):
        forced_name = current_app.config['DEBUG_MONSTER']
        print(f"Debug mode: Forcing monster to {forced_name}")
    session['selected_monster'] = GAME_ENGINE.select_monster(forced_name)  
    return redirect(url_for('game.game_loop'))