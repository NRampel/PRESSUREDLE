from flask import Blueprint, session, request, current_app, redirect, url_for, flash, render_template
from app.services.spotify_serv import music_player as SPOTIFY_SERVICE 
from app.config import Config 


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

#spotify routes go here, they go by this format: @auth_bp.route('/route_name) 

