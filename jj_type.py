import pygame
class Jj_type():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        self.image_0=pygame.image.load("images/jj.jpg")
        self.image_1=pygame.image.load("images/fengyin.png")
        self.rect=self.image_0.get_rect()
        # self.rect=self.image_1.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center=float(self.rect.centerx)
        self.bottom=float(self.rect.bottom)

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=self.ai_settings.jj_speed_factor
        elif self.moving_left and self.rect.left>0:
            self.rect.centerx-=self.ai_settings.jj_speed_factor
        elif self.moving_up:
            self.rect.bottom-=self.ai_settings.jj_speed_factor
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.bottom+=self.ai_settings.jj_speed_factor

    def blitme(self):
        # self.screen.blit(self.image_1,self.rect)
        self.screen.blit(self.image_0,self.rect)

    def center_jj(self):
        self.center=self.screen_rect.centerx