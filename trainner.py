import sys
import tkinter as tk

is_add_life = 0
is_add_score = 0
is_clear_screen = 0
is_save = 0
is_increase_damage = 0
is_increase_enemy_health = 0
is_cancle_enemy_damage = 0
is_can_cancle_enemy_damage = 0
is_infinite_energy = 0
is_large_bullet = 0
is_speed_up = 0

button_texts_col1=[
    'Add Life',
    'Add Score',
    'Clear Screen',
    'Save',
    'Increase Damage',
    'Increase Enemy\'s Health',
    'Cancle Enemy\'s Damage'
]

button_texts_col2 = [
    'Restore Enemy\'s Damage',
    'Infinite Energy',
    'Large Bullet',
    'Speed Up'
]
max_length = max(len(text) for text in button_texts_col1)


def add_life():
    global is_add_life
    is_add_life = 1
def add_score():
    global is_add_score
    is_add_score = 1
def clear_screen():
    global is_clear_screen
    is_clear_screen = 1

def save():
    global is_save
    is_save = 1
def increase_damage():
    global is_increase_damage
    is_increase_damage = 1
def increase_enemy_health():
    global is_increase_enemy_health
    is_increase_enemy_health = 1
def cancle_enemy_damage():
    global is_cancle_enemy_damage
    is_cancle_enemy_damage = 1

def can_cancle_enemy_damage():
    global is_cancle_enemy_damage
    is_cancle_enemy_damage = 0

def infinite_energy():
    global is_infinite_energy
    is_infinite_energy = 1

def large_bullet():
    global is_large_bullet
    is_large_bullet = 1


def speed_up():
    global is_speed_up
    is_speed_up = 1

command_mapping_col1={
    'Add Life' : add_life,
    'Add Score' : add_score,
    'Clear Screen' : clear_screen,
    'Save' : save,
    'Increase Damage' : increase_damage,
    'Increase Enemy\'s Health' : increase_enemy_health,
    'Cancle Enemy\'s Damage' : cancle_enemy_damage
}

command_mapping_col2={
    'Restore Enemy\'s Damage' : can_cancle_enemy_damage,
    'Infinite Energy' : infinite_energy,
    'Large Bullet' : large_bullet,
    'Speed Up' : speed_up
}

def trainner_gui():
    global win
    win=tk.Tk()
    win.geometry('420x210')
    win.minsize(420,210)
    win.maxsize(420,210)
    win.title('Trainner')
    for i,text in enumerate(button_texts_col1,start=1):
        button_width = max_length
        button_col1 = tk.Button(win,padx=20,text=text,command=command_mapping_col1[text],width=button_width)
        button_col1.grid(row=i,column=0,sticky='w')
    for i, text in enumerate(button_texts_col2, start=1):
        button_width = max_length
        button_col2 = tk.Button(win,padx=20,text=text,command=command_mapping_col2[text],width=button_width)
        button_col2.grid(row=i,column=1,sticky='w')
    win.mainloop()



if __name__=='__main__':
    trainner_gui()