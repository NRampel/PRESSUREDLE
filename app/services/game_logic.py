# NOTE: IGNORE ANY IMPORT ERRORS, THAT IS JUST VSCODE TWEAKING OUT FOR NO REASON
import pandas as pd 
import random 
from app.config import Config 

class GameEngine: 
    def __init__(self): 
        self.all_monsters = {}
        self.headers = [] 
        self.numeric_attributes = Config.NUMERIC_ATTRIBUTES
        self._load_monsters((Config.ENTITY_LIST))

    def _load_monsters(self, path):
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip() 
        self.headers = [c for c in df.columns.tolist() if c != 'Name:']
        self.all_monsters = df.set_index('Name:').to_dict(orient='index')
        print("Monsters were successfully loaded!")

    def choose_random_monster(self): 
        return random.choice(list(self.all_monsters.keys()))

    def select_monster(self, monster_name=None):
        if monster_name and monster_name in self.all_monsters: 
            return monster_name
        return self.choose_random_monster()

    def is_valid_guess(self, guess_name): 
        return guess_name in self.all_monsters
    
    def compare_guess(self, guess_name, target): 
        if not self.is_valid_guess(guess_name): 
            return {'ERROR': 'Invalid Monster Name!'}
        
        guess_attributes = self.all_monsters[guess_name] 
        target_attributes = self.all_monsters[target] 
        results = {
            'guess': guess_name,
            'attributes': [], 
            'is_correct': guess_name == target
        }
        for attr in self.headers: 
           guess_val = guess_attributes[attr]
           target_val = target_attributes[attr]
           
           if guess_val == target_val: 
               outcome = 'correct'
           elif attr in self.numeric_attributes: 
               try: 
                     guess_num = float(guess_val)
                     target_num = float(target_val)
                     if guess_num < target_num: 
                          outcome = 'low'
                     else: 
                          outcome = 'high'
               except (ValueError, TypeError): 
                     outcome = 'incorrect'
           else:
               outcome = 'incorrect'
           results['attributes'].append({ 
               'category': attr,
               'guess_value': guess_val,
               'status': outcome
           }) 
        return results 

engine = GameEngine() 