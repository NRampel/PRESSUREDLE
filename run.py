import os
import getpass
from dotenv import load_dotenv
from app import create_app
from app.services.game_logic import engine

load_dotenv()
app = create_app()

def configure_debug_mode():
    if os.environ.get('DEBUG_ACCESS_GRANTED') == 'true':
        print(" [Child Process] ♻️  Reloading with Debug Mode Active...")
        app.config['CHEAT_MODE'] = True
        saved_monster = os.environ.get('DEBUG_MONSTER_NAME')
        if saved_monster:
            app.config['DEBUG_MONSTER'] = saved_monster
        return
    if not os.environ.get('WERKZEUG_RUN_MAIN'):
        debug_password = os.getenv('ADMIN_PSWRD')
        user_input = getpass.getpass("🔒 Enter debug password: ")
        if debug_password and user_input == debug_password:
            print("\n✅ ACCESS GRANTED: Debug Cheats Enabled")
            os.environ['DEBUG_ACCESS_GRANTED'] = 'true'
            app.config['CHEAT_MODE'] = True
            print("\n--- Monster Override ---")
            target_monster = input("Enter monster name to force (or press Enter for random): ").strip()            
            if target_monster:
                if engine.is_valid_guess(target_monster):
                    print(f"🎯 Target Locked: {target_monster}")
                    os.environ['DEBUG_MONSTER_NAME'] = target_monster
                    app.config['DEBUG_MONSTER'] = target_monster
                else:
                    print(f"⚠️ Warning: '{target_monster}' not found. Using random.")
            else:
                print("🎲 Using random monster.")
        else:
            print("\n❌ ACCESS DENIED: Starting in Normal Mode")
            app.config['CHEAT_MODE'] = False
configure_debug_mode()

if __name__ == "__main__":
    app.run()