from flask import jsonify, Blueprint, session
from app.models import discoveredMonsters, User

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/monsters_discovered')
def get_discovered_monsters(): 
    current_user = session.get('user_id')
    if not current_user: 
        return jsonify({}), 401
    monster_list = []
    user_monsters = discoveredMonsters.query.filter_by(user_id=current_user).all()
    for monster in user_monsters:
        monster_list.append({'name': monster.monster_name, 
                             'image_url': f"/static/images/{monster.monster_name}.png"})
    return jsonify(monster_list)