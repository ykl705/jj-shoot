import os
import pickle
from save_loader import load_game
class GameStats():
    def __init__(self,ai_settings):
        if os.path.exists('saves/save.pkl'):
            list=load_game('save.pkl')
            self.high_score=list[1]
            self.species=list[4]+0.0
        else:
            self.high_score=0
            self.species=0.0
        self.ai_settings=ai_settings
        self.reset_stats()
        self.continue_stats()
        self.game_active=False

    def reset_stats(self):
        list = load_game('save.pkl')
        ability_list = load_game('data.pkl')
        self.jj_left=self.ai_settings.jj_limit+ability_list[1]
        self.score=0
        self.energy=0
        self.species = list[4]+0.0
        # self.boss_health=0

    def continue_stats(self):
        if os.path.exists('saves/save.pkl'):
            list=load_game('save.pkl')
            ability_list = load_game('data.pkl')
            self.jj_left =list[2]+ability_list[1]
            self.score =list[0]
            self.energy =list[3]
            self.species = list[4]+0.0
            # self.boss_health =list[4]