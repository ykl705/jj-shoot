import random
import pygame
from pygame.sprite import Sprite
from save_loader import load_game



class Bi(Sprite):
    def __init__(self,ai_settings,screen,enemy_pool_id = 0):
        super(Bi,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.bi_damage = ai_settings.bi_damage
        self.bi_health=ai_settings.bi_health
        self.bi_type=random.randint(1,3)
        type=self.bi_type
        self.enemy_pool_id = enemy_pool_id
        if enemy_pool_id == 1 :
            self.image = pygame.image.load('level/enemy pool/intance_images/money_image.png','level')
        if enemy_pool_id == 2 :
            self.image = pygame.image.load('level/enemy pool/intance_images/magic_image_{0}.png'.format(type), 'level')
        if enemy_pool_id == 3 :
            self.image = pygame.image.load('level/enemy pool/intance_images/virus_image_{0}.png'.format(type), 'level')
        if enemy_pool_id == 0 :
            self.image=pygame.image.load('images/enemy/ren{0}.jpg'.format(type))
        # self.image=pygame.image.load('images/money_image.png')
        self.rect=self.image.get_rect()

        self.rect.x=float(self.rect.width)
        self.rect.y=float(self.rect.height)

        self.x=float(self.rect.x)
        if self.enemy_pool_id != 0 :
            self.y=float(self.rect.y)


    def bi_take_damage(self,damage,ai_settings,stats,bis):
        self.bi_health-=damage
        # print('Left Health : {0}'.format(self.bi_health))
        if self.bi_health <= 0.0:
            stats.score += ai_settings.bi_points
            stats.energy += (ai_settings.bi_points) * 0.5
            self.kill()
        if self.enemy_pool_id == 0 :
            stats.species += float(ai_settings.bi_points )* 0.005
        if self.enemy_pool_id == 1 :
            stats.species += float(ai_settings.bi_points )* 1



    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self,jj):
        # if self.enemy_pool_id == 0:
        #     zx=random.randint(int(-1*self.ai_settings.bi_speed_factor),int(self.ai_settings.bi_speed_factor))
        #     self.x+=zx
        #     self.rect.x=self.x
        #     self.y += self.ai_settings.bi_speed_factor
        #     self.rect.y = self.y
        if self.enemy_pool_id == 0:
            zy=random.randint(1,2)
            if zy==1:
                self.x+=self.ai_settings.bi_speed_factor
                self.rect.x=self.x
            else :
                self.x -= self.ai_settings.bi_speed_factor
                self.rect.x = self.x
            # self.y += self.ai_settings.bi_speed_factor
        elif self.enemy_pool_id == 3 :
            self.x += random.randint(-150,150)
            self.y += random.randint(-150,150)
            self.rect.x = self.x
            self.rect.y = self.y
        if self.enemy_pool_id == 2:
            zy = random.randint(-25, 50)
            self.y +=zy
            self.rect.y = self.y
    def blitme(self):
        self.screen.blit(self.image,self.rect)
