import time
import pygame
from pygame.sprite import Sprite
import random
import tkinter as tk
import game_fuctions as gf
import jj_type
class Boss1(Sprite):
    def __init__(self,ai_settings,screen,jj,bis):
        super(Boss1,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.bi_health = ai_settings.boss1_health
        self.bi_damage = ai_settings.bi_damage
        self.image=pygame.image.load('images/boss/boss1.jpg')
        self.rect=self.image.get_rect()
        self.bi_type = 4
        self.rect.x=float(self.rect.width)
        self.rect.y=float(self.rect.height)

        screen_center_x = self.screen.get_rect().centerx
        screen_center_y = self.screen.get_rect().centery
        self.rect.center = (screen_center_x, screen_center_y)

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)-150


    def bi_take_damage(self,damage,ai_settings,stats,bis):
        stats.energy += 0.1
        self.bi_health-=damage
        move_x = random.randint(-100,100)
        move_y = random.randint(-100,100)
        self.rect.x += move_x
        self.rect.y += move_y
        print('Left Health : {0}'.format(self.bi_health))
        if self.bi_health < 0.0:
            stats.score += 5000
            stats.jj_left += 30
            stats.energy += (ai_settings.bi_points) * 0.5
            stats.species += 200
            self.kill()
            bis.empty()
            # pygame.quit()
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
        self.bi_health += 1
        is_release_skill = random.randint(1,50000)
        if is_release_skill == 5:
            self.rect.x = jj.rect.x
            self.rect.y = jj.rect.y
        zy = random.randint(0, 4)
        if zy == 0:
            self.x += self.ai_settings.bi_speed_factor
            self.rect.x = self.x
        if zy == 1:
            self.x -= self.ai_settings.bi_speed_factor
            self.rect.x = self.x
        if zy == 2:
            self.y += self.ai_settings.bi_speed_factor
            self.rect.y = self.y
        if zy == 3:
            self.y -= self.ai_settings.bi_speed_factor
            self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def kill_boss_screen(self):
        win = tk.Tk()
        win.geometry('120x60+650+300')
        tk.Label(win,text='Congratualation!!!',padx=20,pady=20,foreground='red').pack()
        win.mainloop()