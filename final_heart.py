import time
import pygame
from pygame.sprite import Sprite
import random
import tkinter as tk
import game_fuctions as gf
import jj_type
from special_bi import Special_Bi


number_of_images = 43
heart_images = [pygame.image.load(f'images/heart_pack/image{i}.png') for i in range(number_of_images)]
i = 0

class Final_Heart(Sprite):
    def __init__(self,ai_settings,screen,jj):
        super(Final_Heart,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.bi_health = ai_settings.final_heart_health
        self.bi_damage = ai_settings.bi_damage
        self.image=pygame.image.load('images/heart_pack/image0.png')
        self.rect=self.image.get_rect()
        self.bi_type = 5
        self.rect.x=float(self.rect.width)
        self.rect.y=float(self.rect.height)

        screen_center_x = self.screen.get_rect().centerx
        screen_center_y = self.screen.get_rect().centery-80
        self.rect.center = (screen_center_x, screen_center_y)

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)


    def bi_take_damage(self,damage,ai_settings,stats,bis):
        for i in range(1,15):
            chushou = Special_Bi(ai_settings,self.screen)
            bis.add(chushou)
        stats.energy += 0.1
        self.bi_health-=damage
        print('Left Health : {0}'.format(self.bi_health))
        if self.bi_health < 0.0:
            stats.score += 9999999999
            stats.species += 9999999
            stats.energy += (ai_settings.bi_points) * 0.5
            stats.jj_left += 15000
            self.kill()
            # stats.game_active = False
            # pygame.mouse.set_visible(True)
            # self.kill_boss_screen()

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True



    def update(self,jj):
        self.bi_health += 50
        global i
        i += 1
        # i = random.randint(0,43)
        self.image = pygame.image.load('images/heart_pack/image{0}.png'.format(i%43))
        if i > 43:
            i -= 43
        # self.image = pygame.image.load('images/magic_circle/magic_circle_{0}.png'.format(i%13))
        # if i > 13:
        #     i -= 13
    def blitme(self):
        self.screen.blit(self.image,self.rect)
