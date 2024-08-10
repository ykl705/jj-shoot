import random
import sys
from time import sleep
import pygame
from bullet import Bullet
from bullet import Skill
from bi import Bi
import numpy as np
import save_loader as sl
from boss1_ai import Boss1
from boss2_ai import Boss2
import trainner
import config
from save_loader import load_game
from final_heart import Final_Heart
from boss_virus import Boss_virus
from boss_magic import Boss_Magic

enemy_pool_id = load_game('enemy pool/switch_enemy_pool.pkl','level')

def check_keydown_events(event,ai_settings,screen,stats,sb,jj,bullets,state,filename):
    if event.key==pygame.K_q:
        sl.save_game(state, 'save.pkl')
        sys.exit()
    if event.key == pygame.K_RIGHT:
        jj.moving_right = True
    if event.key == pygame.K_LEFT:
        jj.moving_left = True
    if event.key == pygame.K_UP:
        jj.moving_up = True
    if event.key == pygame.K_DOWN:
        jj.moving_down = True
    if event.key==pygame.K_SPACE:
        new_bullet=Bullet(ai_settings,screen,stats,jj)
        bullets.add(new_bullet)
    if event.key==pygame.K_z and stats.energy >= ai_settings.skill_energy_cost :
        new_bullet=Skill(ai_settings,screen,stats,jj)
        bullets.add(new_bullet)
        stats.energy-=new_bullet.bullet_energy_cost
        sb.prep_energy()
    if event.key==pygame.K_ESCAPE and stats.game_active:
        sl.save_game(state, 'save.pkl')
        stats.game_active = False
        pygame.mouse.set_visible(True)
def check_keyup_events(event,jj):
    if event.key == pygame.K_RIGHT:
        jj.moving_right = False
    if event.key == pygame.K_LEFT:
        jj.moving_left = False
    if event.key == pygame.K_UP:
        jj.moving_up = False
    if event.key == pygame.K_DOWN:
        jj.moving_down = False

def check_events(ai_settings,screen,stats,sb,play_button,continue_button,jj,bis,bullets,state,filename):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,jj)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_button(ai_settings,screen,stats,play_button,continue_button,jj,bis,bullets,mouse_x,mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,jj,bullets,state,filename)

def check_button(ai_settings,screen,stats,play_button,continue_button,jj,bis,bullets,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    button_clicked1=continue_button.rect.collidepoint(mouse_x,mouse_y)
    if (button_clicked or button_clicked1) and not stats.game_active:
        list =load_game('save.pkl')
        stats.high_score=list[1]
        stats.jj_left=list[2]
        stats.score=list[0]
        stats.energy=list[3]
        stats.species=list[4]
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        if play_button.rect.collidepoint(mouse_x,mouse_y):
            stats.reset_stats()
            stats.game_active=True
            bis.empty()
            bullets.empty()
            create_fleet(ai_settings,stats,screen,jj,bis)
            jj.center_jj()
        if continue_button.rect.collidepoint(mouse_x,mouse_y):
            stats.continue_stats()
            stats.game_active=True


def check_fleet_edges(ai_settings,bis):
    for bi in bis.sprites():
        if bi.check_edges():
            change_fleet_direction(ai_settings,bis)
            break

def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()

def change_fleet_direction(ai_settings,bis):
    for bi in bis.sprites():
        # print(ai_settings.fleet_drop_speed1[bi.bi_type-1])
        bi.rect.y+=ai_settings.fleet_drop_speed1[bi.bi_type-1]

def update_screen(ai_settings,screen,stats,sb,jj,bis,bullets,play_button,continue_button,state):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    jj.blitme()
    bis.draw(screen)
    response_to_trainner(ai_settings,stats,bis,bullets,state)
    response_to_config(ai_settings, screen, stats, bis, bullets, state)
    sb.prep_score()
    sb.prep_jj_left()
    sb.show_score()
    sb.prep_species()
    if not stats.game_active:
        play_button.draw_button()
        continue_button.draw_button1()
    pygame.display.flip()

def update_bis(ai_settings,stats,sb,screen,jj,bis,bullets,state):
    check_bis_bottom(ai_settings,stats,screen,jj,bis,bullets)
    check_fleet_edges(ai_settings,bis)
    check_bis_bottom(ai_settings,stats,screen,jj,bis,bullets)
    bis.update(jj)
    if pygame.sprite.spritecollideany(jj,bis):
        ship_hit(ai_settings,stats,sb,screen,jj,bis,bullets,state)

def update_bullets(ai_settings,screen,stats,sb,jj,bis,bullets,bi_number,row_number):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_bi_collisions(ai_settings,screen,stats,sb,jj,bis,bullets,bi_number,row_number)
    # strengthen(ai_settings,stats,screen,jj,bis,bullets)

def check_bullet_bi_collisions(ai_settings,screen,stats,sb,jj,bis,bullets,bi_number,row_number):
    bi = Bi(ai_settings, screen)
    # collisions=pygame.sprite.groupcollide(bullets,bis,bool(strengthen_chuan(ai_settings,stats,screen,jj,bis,bullets)),False)
    # collisions=pygame.sprite.groupcollide(bullets,bis,bool(1),True)
    collisions = pygame.sprite.groupcollide(bullets,bis, False, False)
    if collisions:
        for bullet in collisions.keys():
            if stats.score >=1000:
                pass
            else:
                if bullet.bullet_damage > 500.0:
                    pass
                else:
                    bullet.kill()
        for enemy in collisions.values():
            for bi in enemy:
                bi.bi_take_damage(bullet.bullet_damage,ai_settings,stats,bis)
                if 2700>=stats.score>=2500 or 9000>=stats.score>=7500 and (bi.bi_type==4 or bi.bi_type==5):
                    sb.prep_boss_health(bi.bi_health)
                # stats.score += ai_settings.bi_points
                # stats.energy += (ai_settings.bi_points) * 0.5
                sb.prep_score()
                check_high_score(stats, sb)

                # for bis in collisions.values():
            #     stats.score+=ai_settings.bi_points
            #     stats.energy+=(ai_settings.bi_points)*0.5
            #     bi.bi_health-=ai_settings.bullet_damage
            #     print('left health : {0}'.format(bi.bi_health))
            #     for bi in bis:
            #         if bi.bi_health <= 0:
            #             bi.kill()
            # if(3000>=stats.score>=2500):

            sb.prep_score()
            sb.prep_energy()
        check_high_score(stats,sb)
    if len(bis)<50:
        ai_settings.increase_speed()

def get_number_bis_x(ai_settings,bi_width):
    available_space_x = ai_settings.screen_width - 2 * bi_width
    number_bis_x = int(available_space_x / (2 * bi_width))
    return number_bis_x

def get_number_rows(ai_settings,jj_height,bi_height):
    available_space_y=(ai_settings.screen_height-((3*bi_height)-jj_height))
    number_rows=int(available_space_y/(2*bi_height))
    return number_rows

def create_bi(ai_settings,screen,bis,bi_number,row_number):
    bi = Bi(ai_settings, screen,enemy_pool_id)
    global type
    type=bi.bi_type
    bi_width = bi.rect.width
    bi.x = bi_width + 2 * bi_width * bi_number
    bi.rect.x = bi.x
    bi.rect.y=bi.rect.height+2*bi.rect.height*row_number
    bis.add(bi)



def create_boss(ai_settings,states,screen,jj,bis):
    ability_total = sum(load_game('data.pkl'))
    enemy_pool_id = load_game('enemy pool/switch_enemy_pool.pkl', 'level')
    if 5000 >= states.score >= 2500 and enemy_pool_id ==0 :
        boss = Boss2(ai_settings, screen,jj)
        bis.add(boss)
    if 12000 >= states.score >= 7500 and enemy_pool_id ==0 :
        boss = Boss1(ai_settings, screen, jj,bis)
        bis.add(boss)
    if 100000 >= states.score >= 75000 and enemy_pool_id == 2:
        boss_magic = Boss_Magic(ai_settings,screen,jj,bis)
        bis.add(boss_magic)
    if 200000 >= states.score >150000 and ability_total >= 100 and enemy_pool_id ==0 :
        heart = Final_Heart(ai_settings,screen,jj)
        bis.add(heart)
    if 100000 >= states.score >= 75000 and enemy_pool_id == 3:
        # print(states.score)
        bis.empty()
        boss_virus = Boss_virus(ai_settings,screen,jj,bis)
        bis.add(boss_virus)
def create_fleet(ai_settings,stats,screen,jj,bis):
    bi = Bi(ai_settings, screen)
    number_bis_x=get_number_bis_x(ai_settings,bi.rect.width)
    number_rows=get_number_rows(ai_settings,jj.rect.height,bi.rect.height)

    for row_number in range(number_rows-5):
        for bi_number in np.random.uniform(0,100,int(ai_settings.bi_number)-5):
            if generate_boss(ai_settings,screen,stats,bis) == 10:
                # create_bi(ai_settings, screen, bis, bi_number, row_number)
                bis.empty()
                # create_boss(ai_settings, screen, bis)
            else:
                create_bi(ai_settings,screen,bis,bi_number,row_number)
                if  5000 > stats.score > 2500 or 150000 >= stats.score >= 50000 and enemy_pool_id == 0:
                    if len(bis) > 1:
                        bis.empty()
                        create_boss(ai_settings,stats,screen,jj,bis)
                if  100000 >= stats.score >= 75000 and enemy_pool_id == 3:
                    if len(bis) > 1:
                        bis.empty()
                        create_boss(ai_settings,stats,screen,jj,bis)
                if 12000 >= stats.score >= 7500:
                    create_boss(ai_settings, stats, screen, jj, bis)
                if 100000 >= stats.score >= 75000 and enemy_pool_id == 2:
                    create_boss(ai_settings, stats, screen, jj, bis)
                if stats.score >150000 and enemy_pool_id == 0:
                    if len(bis) > 1:
                        bis.empty()
                    create_boss(ai_settings, stats, screen, jj, bis)

def ship_hit(ai_settings,stats,sb,screen,jj,bis,bullets,state):
    left_str(stats,sb)
    if stats.jj_left>0:
        stats.jj_left-=ai_settings.bi_damage
        sb.prep_jj_left()
        for bi in bis:
            if bi.bi_type != 4:
                bi.kill()
            else :
                pass
        bullets.empty()
        create_fleet(ai_settings,stats,screen,jj,bis)
        jj.center_jj()
        # sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)


i_n = 500

def check_bis_bottom(ai_settings,stats,screen,jj,bis,bullets):
    enemy_pool_id = load_game('enemy pool/switch_enemy_pool.pkl', 'level')
    screen_rect=screen.get_rect()
    # i = random.randint(1,100)
    # if i == 5:
    #     for bi in bis:
    #         bi.kill()
    global i_n
    print('i = ',i_n,'len = ',len(bis))
    if i_n != len(bis):
        i_n = len(bis)
    else:
        if enemy_pool_id != 2 and enemy_pool_id != 3:
            bis.empty()
        else :
            pass
    for bi in bis.sprites():
        if bi.rect.bottom >= screen_rect.bottom or bi.rect.x <= 0 or bi.rect.x >= 700:
            bis.remove(bi)
            if enemy_pool_id ==0 or enemy_pool_id == 1:
                break
                pass
            else :
                pass

def strengthen_chuan(ai_settings,stats,screen,jj,bis,bullets):
    if stats.score>2000:
            return 0
    return 1

def left_str(stats,sb):
    if int(stats.score)%13==0 and stats.score>1:
        stats.jj_left+=1
        sb.prep_jj_left()


def generate_boss(ai_settings,screen,stats,bis):
    # if 150 >= stats.score >= 100 or 5000 >=stats.score >=2500 or 12000 >= stats.score >= 7500:
    #     bis.empty()
    #     return 10
    # else:
    #     return 0
    return 0

def response_to_trainner(ai_settings,stats,bis,bullets,state):
    if trainner.is_add_life == 1:
        stats.jj_left += 1
        trainner.is_add_life = 0
    if trainner.is_add_score == 1:
        stats.score += 100
        trainner.is_add_score= 0
    if trainner.is_clear_screen == 1:
        bis.empty()
        trainner.is_clear_screen= 0
    if trainner.is_save == 1:
        sl.save_game(state, 'save.pkl')
        trainner.is_save= 0
    if trainner.is_increase_damage == 1:
        ai_settings.bullet_damage *= 2
        trainner.is_increase_damage= 0
    if trainner.is_increase_enemy_health == 1:
        ai_settings.bi_health += 10
        trainner.is_increase_enemy_health = 0
    if trainner.is_cancle_enemy_damage == 1:
        ai_settings.bi_damage = 0
    if trainner.is_cancle_enemy_damage == 0:
        ai_settings.bi_damage = 1
    if trainner.is_infinite_energy == 1:
        ai_settings.skill_energy_cost = 0
    if trainner.is_large_bullet == 1:
        ai_settings.bullet_width *= 2
        ai_settings.bullet_height *= 2
        trainner.is_large_bullet = 0
    if trainner.is_speed_up ==1:
        ai_settings.bi_speed_factor +=1
        trainner.is_speed_up =0

def response_to_config(ai_settings,screen,stats,bis,bullets,state):
    if config.is_full_screen == 1:
        pygame.display.toggle_fullscreen()
        pygame.display.flip()
        config.is_full_screen = 0
    # if config.is_full_screen == 1:
    #     full_screen_width, full_screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    #     ai_settings.screen_width = full_screen_width
    #     ai_settings.screen_height= full_screen_height
    #     # screen = pygame.display.set_mode((full_screen_width, full_screen_height), flags=pygame.FULLSCREEN)


def random_event_inside(ai_settings,screen,stats,sb,jj,bis,bullets,play_button,continue_button,state):
    if stats.score >= 5000 :
        is_event = random.randint(1,99999999)
        if 50000 <= is_event <= 50002:
            pass
