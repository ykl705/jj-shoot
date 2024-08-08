import pygame
from pygame.sprite import Sprite
import tkinter as tk

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,stats,jj):
        super(Bullet,self).__init__()
        self.screen=screen
        self.bullet_damage=ai_settings.bullet_damage
        self.is_bullet_penetrate=ai_settings.bullet_penetrate
        self.bullet_energy_cost=ai_settings.bullet_energy_cost
        # print(stats.score)
        if stats.score>500:
            i=3
        else:
            i=1
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width*i,ai_settings.bullet_height)
        self.rect.centerx=jj.rect.centerx
        self.rect.top=jj.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        # self.x+=self.speed_factor
        self.y-=self.speed_factor
        self.rect.y=self.y
        # self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        # pygame.draw.rect(self.screen,self.color,self.rect)
        # pygame.draw.rect(self.screen,self.color,self.rect)


class Skill(Sprite):
    def __init__(self,ai_settings,screen,stats,jj):
        super(Skill,self).__init__()
        self.screen=screen
        self.bullet_damage=ai_settings.skill_damage
        self.is_bullet_penetrate=ai_settings.skill_penetrate
        self.bullet_energy_cost = ai_settings.skill_energy_cost
        if stats.score>500:
            i=3
        else:
            i=1
        self.rect=pygame.Rect(0,0,ai_settings.skill_width*i,ai_settings.skill_height)
        self.rect.centerx=jj.rect.centerx
        self.rect.top=jj.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        # self.x+=self.speed_factor
        self.y-=self.speed_factor
        self.rect.y=self.y
        # self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,self.color,self.rect)