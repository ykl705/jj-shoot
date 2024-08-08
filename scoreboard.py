import pygame.font
from save_loader import load_game
import os

class Scoreboard():
    def __init__(self,ai_settings,screen,stats,bi):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,24)
        if 2700 >= stats.score >= 2500:
            print(ai_settings.boss2_health)
            self.boss_total_health = 7500.0
        if 12000 >= stats.score >=7500:
            self.boss_total_health = 100000.0
        else :
            self.boss_total_health = ai_settings.bi_health
        self.prep_score()
        self.prep_high_score()
        self.prep_energy()
        self.prep_jj_left()
        self.prep_boss_health(bi.bi_health)
        self.prep_species()

    def prep_score(self):
        rounded_score = int(self.stats.score)
        score_str = "score:{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def prep_high_score(self):
        high_score=int(self.stats.high_score)
        high_score_str="highest score:{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top


    def prep_energy(self):
        energy=int(self.stats.energy)
        energy_str="energy:{:,}".format(energy)
        self.energy_image=self.font.render(energy_str,True,self.text_color,self.ai_settings.bg_color)

        self.energy_rect=self.high_score_image.get_rect()
        self.energy_rect.centerx=self.screen_rect.centerx-240
        self.energy_rect.top=20


    def prep_jj_left(self):
        jj_left=int(self.stats.jj_left)
        jj_left_str="jj left:{:,}".format(jj_left)
        self.jj_left_image=self.font.render(jj_left_str,True,self.text_color,self.ai_settings.bg_color)

        self.jj_left_rect=self.jj_left_image.get_rect()
        self.jj_left_rect.centerx=self.screen_rect.centerx-280
        # self.high_score_rect.top=40

    def prep_boss_health(self,bi_health):
        boss_health=float(bi_health)*100/self.boss_total_health
        if bi_health >= 99999999:
            boss_health_str="boss health: ??????????????".format(boss_health)
        else :
            boss_health_str="boss health:{:,}%".format(boss_health)
        self.boss_health_image=self.font.render(boss_health_str,True,self.text_color,self.ai_settings.bg_color)

        self.boss_health_rect=self.boss_health_image.get_rect()
        self.boss_health_rect.centerx=self.screen_rect.centerx


    def prep_species(self):
        species=int(self.stats.species)
        species_str='money:{:,}'.format(species)
        self.species_image=self.font.render(species_str,True,self.text_color,self.ai_settings.bg_color)

        self.species_rect=self.species_image.get_rect()
        self.species_rect.right=self.screen_rect.right-20
        self.species_rect.top = 0

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.energy_image,self.energy_rect)
        self.screen.blit(self.jj_left_image,self.jj_left_rect)
        self.screen.blit(self.boss_health_image,self.boss_health_rect)
        self.screen.blit(self.species_image,self.species_rect)