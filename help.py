import tkinter as tk

def help():
    win=tk.Tk()
    win.geometry('600x360+650+300')
    win.minsize(600,360)
    win.maxsize(600,360)
    text=tk.Label(win,text="Press Space to Shoot\n\n"
                       "Press up down left right to Move\n\n"
                       "Press q to quit\n\n"
                       "You only Have 20 Opportunities\n\n"
                       "It will be more and more Difficult with Playing\n\n"
                       "JJ left can Incrase when Achieving Specific Scores\n\n"
                       "You can Press z and Consume 50 energy to Release Skill\n\n"
                       "If you Wanna Pause ,Press esc\n\n"
                        "There are three boss in normal mode,the final boss need some condition").pack()
    button=tk.Button(win,text='Quit',padx=5,command=lambda :quit(win),width=15,height=1)
    button.pack()
    win.mainloop()

def quit(win):
    win.withdraw()
    win.quit()

if __name__ =='__main__':
    help()