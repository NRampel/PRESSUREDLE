import spotipy as sp 
import os
from spotipy.oauth2 import SpotifyOAuth 
from app.config import Config 

class SpotifyService: 
    def __init__(self): 
        self.client_id = Config.SPOT_CLIENT_ID
        self.client_secret = Config.SPOT_CLIENT_SEC
        self.redirect_url = Config.SPOT_REDIRECT_URL 
    
    def initialize_spotify_client(self): 
        return sp.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_url, 
            scope="user-library-read user-top-read"
        )) 


music_player= SpotifyService() 