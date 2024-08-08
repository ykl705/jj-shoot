import pygame
import tkinter as tk
from pygame.sprite import Group
import threading
from settings import Settings
from jj_type import Jj_type
import game_fuctions as gf
from bi import Bi
from game_stats import GameStats
from scoreboard import Scoreboard
from music_loader import musicLoader
from config import config_panel
from help import help
from trainner import trainner_gui
from purchase_ability import shop_gui
from illustrated_handbook import illustrated_handbook_gui
from quit import quit
from button import Button
from button1 import Button1
from save_loader import load_game
from gacha import gacha
from level import level_switcher
from pack import pcak_gui
from choose_jj import choose_jj_gui
import config
from boss1_ai import Boss1
from boss2_ai import Boss2


pygame.init()
fps=45
fclock=pygame.time.Clock()
ai_settings = Settings()
stats = GameStats(ai_settings)
state = [stats.score, stats.high_score, stats.jj_left, stats.energy, stats.species]
enemy_pool_id = load_game('enemy pool/switch_enemy_pool.pkl','level')


intance_id = 1
def run_game():

    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    icon=pygame.image.load('images/jj.jpg')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("jj__shoot")
    play_button = Button(ai_settings, screen, 'Replay')
    continue_button = Button1(ai_settings, screen, 'Continue')
    global states
    stats = GameStats(ai_settings)
    bi = Bi(ai_settings, screen,enemy_pool_id)
    sb = Scoreboard(ai_settings, screen, stats,bi)
    jj = Jj_type(ai_settings, screen)
    bullets = Group()
    bis = Group()
    # bosses = Group()
    gf.create_fleet(ai_settings,stats,screen,jj,bis)
    ability_list = load_game('data.pkl')
    while True:
        state=[float]
        state=[stats.score,stats.high_score,stats.jj_left,stats.energy,stats.species]
        gf.check_events(ai_settings,screen,stats,sb,play_button,continue_button,jj,bis,bullets,state,'save.pkl')
        if stats.game_active:
            print(len(bis))
            if len(bis)<100+ability_list[0]:
                gf.create_fleet(ai_settings,stats,screen, jj, bis)
            jj.update()
            gf.update_bullets(ai_settings,screen,stats,sb,jj,bis,bullets,gf.get_number_bis_x(ai_settings,bi.rect.width),gf.get_number_rows(ai_settings,jj.rect.height,bi.rect.height))
            gf.update_bis(ai_settings,stats,sb,screen,jj,bis,bullets,state)
        gf.update_screen(ai_settings,screen,stats,sb,jj,bis,bullets,play_button,continue_button,state)
        # print(len(bis))
        fclock.tick(fps)
        pygame.display.update()




# win=tk.Tk()
# win.title('introduction')
# win.geometry('360x240+650+300')
# play_button = tk.Button(win,padx=20,text='Play Now',command=lambda :run_game())

# play_button.pack()
# choose_music_button = tk.Button(win, padx=20, text="Choose Music", command=lambda: musicLoader())
# choose_music_button.pack()
# help_button=tk.Button(win,padx=20,text="Help",command=lambda: help())
# help_button.pack()

button_texts_col1 = ['Play Now', 'Choose Music', 'Config', 'Help', 'Trainner', 'Illustred', 'Quit']
button_texts_col2 = ['Gacha','Intance','Pack','Choose jj']
max_length = max(len(text) for text in button_texts_col1)
def run_game_wrapper():
    threading.Thread(target=run_game).start()

win = tk.Tk()
win.title('Menu')
win.geometry('360x240+650+300')
win.minsize(360,240)
win.maxsize(360,240)

command_mapping_col1 = {
    'Play Now': run_game_wrapper,
    'Choose Music': musicLoader,
    'Config' : config_panel,
    'Help': help,
    'Trainner' : trainner_gui,
    'Illustred' : illustrated_handbook_gui,
    'Quit' : quit
}
command_mapping_col2 = {
    'Gacha' : gacha,
    'Intance' : level_switcher.switcher_gui,
    'Pack' : pcak_gui,
    'Choose jj' : choose_jj_gui
}

for i, text in enumerate(button_texts_col1, start=1):
    button_width = max_length
    button = tk.Button(win, padx=20, text=text, command=command_mapping_col1[text], width=button_width)
    button.grid(row=i, column=0, sticky='w')
button = tk.Button(win,text='Purchasse Ability',command=lambda :shop_gui(stats,state),width=17).grid()
for i,text in enumerate(button_texts_col2,start=1):
    button_width = max_length
    button = tk.Button(win,padx=20,text=text,command=command_mapping_col2[text],width=button_width)
    button.grid(row=i,column=1,sticky='w')
win.mainloop()

