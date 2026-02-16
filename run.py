
import os
import getpass
from dotenv import load_dotenv
from app import create_app
from app.services.game_logic import engine

load_dotenv()
app = create_app()

def configure_debug_mode():
    if os.getenv('DEBUG_ACCESS_GRANTED') == 'true':
        print(" [Child Process] ♻️  Reloading with Debug Mode Active...")
        app.config['CHEAT_MODE'] = True
        saved_monster = os.environ.get('DEBUG_MONSTER_NAME')
        if saved_monster:
            app.config['DEBUG_MONSTER'] = saved_monster
        return
    if not os.environ.get('WERKZEUG_RUN_MAIN'):
        debug_password = os.getenv('ADMIN_PSWRD')
        if debug_password: 
             user_input = getpass.getpass("🔒 Enter debug password: ")
        else:
             user_input = getpass.getpass("🔒 Enter debug password (default 1234): ")
             debug_password = "1234"

        if user_input == debug_password:
            print("\n✅ ACCESS GRANTED: Debug Cheats Enabled")
            os.environ['DEBUG_ACCESS_GRANTED'] = 'true'
            app.config['CHEAT_MODE'] = True
            
            print("\n--- Monster Override ---")
            raw_monster = input("Enter monster name to force (or press Enter for random): ").strip()
            
            if raw_monster:
                if engine.is_valid_guess(raw_monster):
                    real_name = engine.select_monster(raw_monster) 
                    
                    print(f"🎯 Target Locked: {real_name}")
                    os.environ['DEBUG_MONSTER_NAME'] = real_name
                    app.config['DEBUG_MONSTER'] = real_name
                else:
                    print(f"⚠️ Warning: '{raw_monster}' not found. Using random.")
            else:
                print("🎲 Using random monster.")
        else:
            print("\n❌ ACCESS DENIED: Starting in Normal Mode")
            app.config['CHEAT_MODE'] = False
configure_debug_mode()

if __name__ == "__main__":
    app.run()