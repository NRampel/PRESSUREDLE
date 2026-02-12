from flask import Blueprint, render_template, request, redirect, session, url_for 
import sqlalchemy
from app.models import User
from app import db


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if 'user' in session: 
        return redirect(url_for('game.default'))
    if request.method == 'POST':
        raw_name = request.form.get('username', '')
        username = " ".join(raw_name.split()).title()
        if not username: 
            return render_template('entername.html', error="Name must not be empty!")
     
        user = User.query.filter_by(username=username).first()
        if not user: 
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        session['user'] = username 
        session['user_id'] = user.id 
        return redirect(url_for('game.default')) 
    return render_template('entername.html')

@auth_bp.route('/logout', methods=['POST', 'GET'])
def logout(): 
    session.clear() 
    return redirect(url_for('auth.login'))

