import tkinter as tk
import random
from PIL import Image,ImageTk

emeny_images_set = {
    1:'images/enemy/ren1.png',
    2:'images/enemy/ren2.png',
    3:'images/enemy/ren3.png',
    4:'images/boss/boss2.png',
    5:'images/boss/boss1.png'
}

emeny_name_set = {
    1:'Stick Figure',
    2:'Chest',
    3:'Bi',
    4:'Black Hole',
    5:'Malignant Proliferation'
}


emeny_introductin_text_set = {
    1:'A simple  emeny whithout any ability\nwhose speed is low',
    2:'A compact emeny whithout any ability\nwhich moves a bot fast',
    3:'The most common emeny\nIt don\'t have any ability',
    4:'A mysterious being.\nits power can distort the space',
    5:'A lump of disgusting tissue,\n\'they\' have horrible regenerated ability'
}

emeny_cookie_text_set = {
    1:'Still remember the stick figure we drew before ?',
    2:'Maybe not hot ?',
    3:'Guess what',
    4:'It just wanna swallow your jj',
    5:'Fright a quick battle,guy !'
}


def illustrated_handbook_gui():
    win = tk.Toplevel()
    win.geometry('375x210')
    win.minsize(375,210)
    win.maxsize(375,210)
    for i in emeny_images_set:
        image_path = emeny_images_set[i]
        try:
            image = tk.PhotoImage(file=image_path)
            button = tk.Button(win,image=image, command=lambda id=i: show_introduction(id, image,win))
            button.image = image
            button.grid(row=1, column=i, sticky='w')
        except tk.TclError as e:
            print(f"Failed to load image for enemy {i}: {e}")

    win.mainloop()

def show_introduction(id, image,win):
    win = tk.Toplevel(win)
    tk.Label(win, text=emeny_name_set[id]).pack()
    # image = emeny_images_set[id]
    # image = tk.PhotoImage(file=image_path)
    image = Image.open(emeny_images_set[id])
    photo = ImageTk.PhotoImage(image)
    tk.Label(win,image=photo).pack()
    tk.Label(win, text=emeny_introductin_text_set[id], pady=10).pack()
    tk.Label(win, text=emeny_cookie_text_set[id], pady=30, fg='green').pack()
    win.mainloop()






# def show_introduction(id):
#     win=tk.Tk()
#     tk.Label(win,text=emeny_name_set[id]).pack()
#     tk.Label(win,text=emeny_introductin_text_set[id],pady=10).pack()
#     tk.Label(win,text=emeny_cookie_text_set[id],pady=30,fg='green').pack()
#     win.geometry('300x180+650+300')
#     win.mainloop()

if __name__ == '__main__':
    illustrated_handbook_gui()