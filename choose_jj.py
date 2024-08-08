import tkinter as tk



def choose_jj_gui():
    win = tk.Toplevel()
    win.geometry('260x320+400+350')
    win.minsize(260,300)
    win.maxsize(260,300)
    tk.Label(win,text='施工中').pack()
    win.mainloop()




if __name__ == '__main__':
    choose_jj_gui()