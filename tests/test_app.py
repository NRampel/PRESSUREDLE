import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.game_logic import GameEngine

def test_game_logic(): 
    try: 
        engine = GameEngine() 
        assert engine is not None 
        print("Engine successful")
    except Exception as e:
        assert False, f"Engine initialization failed: {e}"