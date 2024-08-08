import tkinter as tk
import pygame
from settings import Settings
import config
ai_settings=Settings()
def musicLoader():
    win=tk.Tk()
    win.geometry("275x200")
    win.minsize(275,200)
    win.maxsize(275,200)
    for i in range(0,15):
        button_width = 20
        button = tk.Button(win,padx=20,text='music{0}'.format(i),command=lambda :music_id(i%4,win))
        button.grid(row=i%5,column=int(i/5),sticky='w')
    button = tk.Button(win,text='Stop Music',command=lambda :stop_play_music(),width=11)
    button.grid(row=6, column=0)
    button = tk.Button(win,text='Quit',command=lambda :quit(win),width=11)
    button.grid(row=6, column=2)
    win.mainloop()

def music_id(num,win):
    print(num)
    pygame.init()
    pygame.mixer.music.load('music/bgm{0}.ogg'.format(num))
    print(float(config.music_volume)/100.0)
    pygame.mixer.music.play(-1)
    win.withdraw()
    win.quit()

def stop_play_music():
    pygame.mixer.music.stop()

def quit(win):
    win.withdraw()
    win.quit()