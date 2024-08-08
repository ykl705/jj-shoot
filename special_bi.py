import random
import pygame
from pygame.sprite import Sprite

class Special_Bi(Sprite):
    def __init__(self,ai_settings,screen):
        super(Special_Bi,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.bi_damage = ai_settings.bi_damage
        self.bi_type = 4
        self.bi_health=ai_settings.bi_health
        self.image=pygame.image.load('images/chushou.jpg'.format(type))
        self.rect=self.image.get_rect()

        screen_center_x = self.screen.get_rect().centerx
        screen_center_y = self.screen.get_rect().centery
        self.rect.center = (screen_center_x, screen_center_y)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def bi_take_damage(self,damage,ai_settings,stats,bis):
        self.bi_health -= 0
        # print('Left Health : {0}'.format(self.bi_health))
        if self.bi_health < 0.0:
            stats.score += ai_settings.bi_points
            stats.energy += (ai_settings.bi_points) * 0.5
            stats.species += float(ai_settings.bi_points )* 0.005
            self.kill()


    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self,jj):
        i =random.randint(-250,250)
        j =random.randint(-250,250)
        self.x += i
        self.y += j
        self.rect.x = self.x
        self.rect.y = self.y
        # zy = random.randint(0, 2)
        # if zy == 0:
        #     self.x += i
        #     self.rect.x = self.x
        # if zy == 1:
        #     self.x -= i
        #     self.rect.x = self.x
        # if zy == 2:
        #     self.y += i
        #     self.rect.y = self.y
        # if zy == 3:
        #     self.y -= i
        #     self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)
