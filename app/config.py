import os 
from dotenv import load_dotenv


load_dotenv() 

class Config: 
    SECRET_KEY = os.getenv('KEY', 'Developer_Key')
    SPOT_CLIENT_ID = os.getenv("SPOT_CLIENT_ID")
    SPOT_CLIENT_SEC = os.getenv("SPOT_CLIENT_SEC")
    SPOT_REDIRECT_URL = os.getenv("SPOT_REDIRECT_URL")
    ENTITY_LIST = os.getenv('MONSTER_PATH', 'monsters.csv')
    NUMERIC_ATTRIBUTES = ['Damage', 'Speed']
    DIFFICULTY = {
        'easy': 12, 
        'medium': 9, 
        'hard': 5
    }
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
