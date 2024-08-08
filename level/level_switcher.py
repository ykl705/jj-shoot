import sys
import tkinter as tk
from PIL import Image,ImageTk
import save_loader


enemy_pool_id = save_loader.load_game('switch_enemy_pool.pkl','level/enemy pool')
print(enemy_pool_id)

intance_name_set = {
    1 : 'Species Intance',
    2 : 'Magic Intance(高难)',
    3 : 'Biochemistry Intance(高难)'
}

i = 1
def switcher_gui(i=1):
    win = tk.Toplevel()
    # win = tk.Tk()
    win.geometry('260x330+400+350')
    win.minsize(260,330)
    win.maxsize(260,330)
    tk.Label(win,text='Intance').grid(row=1,column=2)
    image = Image.open('level/images/intance_image_{0}.png'.format(i))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(win,image=photo)
    image_label.photo = photo
    image_label.grid(row=2,column=2)
    button = tk.Button(win,text='Choose',command=lambda :choose_intance(win,i)).grid(row=3,column=2)
    button = tk.Button(win,text='<=',command=lambda :left_turn(win,i)).grid(row=4,column=0,sticky='s')
    button = tk.Button(win,text='=>',command=lambda :right_turn(win,i)).grid(row=4,column=3,sticky='s')
    text = tk.Label(win,text=intance_name_set[i],fg='orange').grid(row=5,column=2)
    win.mainloop()



def right_turn(win,i):
    win.destroy()
    if i < 3 :
        i += 1
    win.after(1,switcher_gui(i))
def left_turn(win,i):
    win.destroy()
    if i > 1 :
        i -= 1
    win.after(1,switcher_gui(i))


def choose_intance(win,i):
    enemy_pool_id = save_loader.load_game('switch_enemy_pool.pkl','level/enemy pool')
    if enemy_pool_id != i :
        enemy_pool_id = i
    else :
        enemy_pool_id = 0
    print("enemy_pool_id = ",enemy_pool_id)
    save_loader.save_game(enemy_pool_id,'switch_enemy_pool.pkl','level/enemy pool')
    win.destroy()

    sys.exit()



if __name__ == "__main__":
    switcher_gui(i)