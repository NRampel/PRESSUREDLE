from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def user_greet():
    return render_template('greeting.html')

@main_bp.route('/about')
def about(): 
    return render_template('about.html')

@main_bp.route('/attrtibutes')
def view_attributes():
    return render_template('attributes.html')