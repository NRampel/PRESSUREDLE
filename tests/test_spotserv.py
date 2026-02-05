import os 
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.spotify_serv import SpotifyService
def test_spotify_service(): 
    try: 
        spot_server = SpotifyService() 
        assert spot_server is not None
        print("Spotify server uploaded") 
    except Exception as e: 
        assert False, f"Spotify service initialization failed: {e}"