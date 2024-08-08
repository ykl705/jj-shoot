import tkinter as tk
from save_loader import load_game

pack_set = load_game('pack.pkl')


def pcak_gui():
    win = tk.Toplevel()
    win.geometry('260x300')
    win.minsize(260,300)
    win.maxsize(260,300)
    win.title('Pack')
    tk.Label(win,text='Pack 施工中',width=35).grid(row=1)
    # for i in pack_set:
    for i,text in enumerate(pack_set,start=1):
        # print(type(pack_set[text]))
        text = tk.Label(win,text=text+'   :   '+str(pack_set[text]))
        text.grid(row=i+1,column=0,sticky='w')
        # print(type(i),type(pack_set[i]))
    win.mainloop()


if __name__ == '__main__':
    pcak_gui()