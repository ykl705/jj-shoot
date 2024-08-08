import datetime
import tkinter as tk
import save_loader
import random
import pygame
from PIL import Image,ImageTk




banner = save_loader.load_game('banner.pkl')
data = save_loader.load_game('data.pkl')
save = save_loader.load_game('save.pkl')




def gacha():
    global win
    # win = tk.Tk()
    win = tk.Toplevel()
    win.geometry('375x210+600+400')
    win.minsize(375,210)
    win.maxsize(375,210)
    image = Image.open('images/gift_box.png')
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(win,image=photo)
    image_label.photo = photo
    image_label.pack()
    tk.Label(win,text='Daily Gacha!!',fg='red').pack()
    tk.Button(win,text='Click Me',command=lambda :generate_random_item(),width=15).pack(side="top", expand=True)
    win.mainloop()






def is_suitable():
    now_time =datetime.datetime.now()
    ls1=str(now_time).split(' ')
    flag=save_loader.load_game('date.pkl')
    if ls1[0]!=flag[0]:
        flag=ls1
        save_loader.save_game(flag,'date.pkl')
        return 1
    else :
        return 0


def generate_random_item():
    pygame.init()
    pygame.mixer.init()
    if is_suitable() :
        id = random.randint(0,7)
        win = tk.Tk()
        win.geometry('+700+500')
        if id == 0 :
            save[4] += 500
            save_loader.save_game(save,'save.pkl')
            pygame.mixer.music.load('music/win.ogg')
            pygame.mixer.music.play(-1)
        if id == 1:
            level_up = random.randint(0,6)
            data[level_up] += 1
            save_loader.save_game(data,'data.pkl')
            pygame.mixer.music.load('music/win.ogg')
            pygame.mixer.music.play(-1)
        tk.Label(win,text='Congratulation!!!\nYou have got :\n{0}'.format(banner[id]),fg='red').pack(side="top", expand=True)
        win.mainloop()

    else :
        win = tk.Tk()
        win.geometry('+700+500')
        tk.Label(win,text='You have gachaed today!').pack()
        win.mainloop()




if __name__ == '__main__' :
    # pass
    gacha()
    # is_suitable()
    # generate_random_item()
