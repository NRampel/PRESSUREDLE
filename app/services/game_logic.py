# NOTE: IGNORE ANY IMPORT ERRORS, THAT IS JUST VSCODE TWEAKING OUT FOR NO REASON
import pandas as pd 
import random 
from app.config import Config 

class GameEngine: 
    def __init__(self): 
        self.all_monsters = pd.DataFrame() 
        self.headers = [] 
        self.numeric_attributes = Config.NUMERIC_ATTRIBUTES
        self._load_monsters((Config.ENTITY_LIST))

    def _load_monsters(self, path):
        self.all_monsters = pd.read_csv(path)
        self.all_monsters.columns = self.all_monsters.columns.str.strip() 
        self.all_monsters.set_index('Name:', inplace=True)
        self.headers = self.all_monsters.columns.tolist() 
        print("Monsters were successfully loaded!")

    def choose_random_monster(self): 
        return random.choice(self.all_monsters.index)

    def is_valid_guess(self, guess_name): 
        return guess_name in self.all_monsters.index
    
    def compare_guess(self, guess_name, target): 
        if not self.is_valid_guess(guess_name): 
            return {'ERROR': 'Invalid Monster Name!'}
        
        guess_attributes = self.all_monsters.loc[guess_name] 
        target_attributes = self.all_monsters.loc[target] 
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