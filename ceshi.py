import threading
from tqdm import *
import save_loader
n = 0
def add():
    global n
    for i in range(1,10000001):
        n+=1
def add1():
    for i in range(1,11):
        threading.Thread(target=add())
def f():
    for i in tqdm(range(1,11)):
        threading.Thread(target=add1())
        print(n)

def f1():
    global n
    for i in tqdm(range(1,1000000001)):
        n+=1
    print(n)

# f1()
# f()

# list = save_loader.load_game('data.pkl')
# for i in range(0,4):
#     print(list[i])

state = save_loader.load_game('species_intance_enemy_pool.pkl','level/enemy pool')
print(state)