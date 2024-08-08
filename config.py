import tkinter as tk

music_volume = 10
is_full_screen = 0
is_cancle_full_screen = 0
def update_music_volume():
    new_value = scale.get()
    global music_volumeq
    music_volume= new_value
    value_label.config(text=f"Volume: {music_volume}")

def full_screen():
    global is_full_screen
    is_full_screen = 1

def config_panel():
    win = tk.Tk()
    win.title('Config')
    win.geometry('400x300')
    win.minsize(400,300)
    win.maxsize(400,300)
    global scale
    global value_label
    scale = tk.Scale(win, from_=0, to=100, orient='horizontal', length=300)
    value_label = tk.Label(win, text=f"Volume : {scale.get()}")
    value_label.pack()
    scale.pack(pady=0)
    scale.bind("<Motion>", update_music_volume())

    button=tk.Button(win,text='FullScreen//CancleFullScreen',command=lambda :full_screen())
    button.pack()
    win.mainloop()

if __name__ == '__main__':
    config_panel()