import os, getpass
from dotenv import load_dotenv
from app import create_app, db
from app.services.game_logic import engine

load_dotenv()
app = create_app()


def configure_debug():
    if os.getenv('DEBUG_ACCESS_GRANTED') == 'true':
        print(" [Child] ♻️  Reloading with Debug Mode...")
        app.config['CHEAT_MODE'] = True
        if m := os.environ.get('DEBUG_MONSTER_NAME'): app.config['DEBUG_MONSTER'] = m
        return True

    if not os.environ.get('WERKZEUG_RUN_MAIN'):
        pwd = os.getenv('ADMIN_PSWRD')
        prompt = f"🔒 Enter debug password: "
        
        if getpass.getpass(prompt) == pwd:
            print("\n✅ ACCESS GRANTED: Debug Cheats Enabled\n\n--- Monster Override ---")
            os.environ['DEBUG_ACCESS_GRANTED'] = 'true'
            app.config['CHEAT_MODE'] = True
            
            if (m := input("Enter monster name to force (or press Enter for random): ").strip()) and engine.is_valid_guess(m):
                real = engine.select_monster(m)
                print(f"🎯 Target Locked: {real}")
                os.environ['DEBUG_MONSTER_NAME'] = app.config['DEBUG_MONSTER'] = real
            else:
                print("🎲 Using random monster.")
            return True
        print("\n❌ ACCESS DENIED: Starting in Normal Mode")
    
    app.config['CHEAT_MODE'] = False
    return False

if __name__ == "__main__":
    app.run(debug=configure_debug())