import sys
import tkinter as tk
from save_loader import save_game
from save_loader import load_game
goods_name_set = {
    1:'Lust',
    2:'Gluttony',
    3:'Greed',
    4:'Sloth',
    5:'Wrath'
}
goods_price_set  = {
    1:50,
    2:50,
    3:50,
    4:50,
    5:50
}


ability_list = load_game('data.pkl')
win = None
def shop_gui(states,state):
    global win
    if win:
        win.quit()
    win=tk.Tk()
    win.title('Strengthen')
    win.geometry('330x260+650+300')
    win.minsize(330,260)
    win.maxsize(330,260)
    tk.Label(win,text=str('money : '+str(state[4]))).grid(column=3)
    button_width = 12
    for i,text in enumerate(goods_name_set,start=1):
        button = tk.Button(win,text=goods_name_set[text]+'\n{0}'.format(goods_price_set[i]),command=lambda id=i:buy_good(states,id,win,state),width=button_width)
        button.grid(row=i,column=0,sticky='w')
    button = tk.Button(win,text='Reset Ability',command=lambda :reset_ability(states,win,state),width=button_width,height=2)
    button.grid(row=1,column=1,sticky='w')
    win.mainloop()
    # win.after(1, shop_gui(states, state))

def reset_ability(states,win,state):
    win.destroy()
    ability_list = load_game('data.pkl')
    states.species+=ability_list[5]*50
    ability_list[5] = 0
    save_game(ability_list,'data.pkl')
    ability_list=[0,0,0,0,0,0]
    state[4]=states.species
    save_game(state,'save.pkl')
    save_game(ability_list,'data.pkl')
    win.after(1, shop_gui(states, state))


def buy_good(states,id,win,state):
    win.destroy()
    list = [50,50,50,50,50]
    if states.species >= list[id-1]:
        states.species -= list[id-1]
        print(states.species)
        print('id = '+str(id))
        if id==1:
            ability_list[0]+=5
            ability_list[5]+=1
            print(ability_list[0])
            save_game(ability_list, 'data.pkl')
        if id==2:
            ability_list[1]+=1
            ability_list[5] += 1
            save_game(ability_list, 'data.pkl')
        if id==3:
            ability_list[2]+=2
            ability_list[5] += 1
            save_game(ability_list, 'data.pkl')
        if id==4:
            ability_list[3]+=0.02
            ability_list[5] += 1
            save_game(ability_list, 'data.pkl')
        if id==5:
            ability_list[4]+=3
            ability_list[5] += 1
            save_game(ability_list, 'data.pkl')
        state[4]=states.species
        save_game(state,'save.pkl')
    win.after(1, shop_gui(states, state))
        # win.quit()
        # win.update_idletasks()
        # win.update()
