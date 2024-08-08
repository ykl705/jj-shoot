import pickle
import os

def save_game(stats,filename,save_dir='saves'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    filepath=os.path.join(save_dir,filename)
    with open(filepath,'wb') as f:
        pickle.dump(stats,f)

def load_game(filename,save_dir='saves'):
    filepath=os.path.join(save_dir,filename)
    with open(filepath,'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    pass
    # state = 0
    # state = {
    #     'Money' : 0,
    #     '施工中1' : 0,
    #     '施工中2' : 0,
    #     '施工中3' : 0,
    #     '施工中4' : 0,
    #     '施工中5' : 0,
    #     '施工中6' : 0,
    #     '施工中7' : 0,
    #     '施工中8' : 0
    # }
    # state = [0, 0, 0, 0, 10000000,0]
    # state = {
    #     0:'Species + 500',
    #     1:'A random ability up',
    #     2:'啥也没有',
    #     3:'啥也没有',
    #     4:'啥也没有',
    #     5:'啥也没有',
    #     6:'啥也没有',
    #     7:'啥也没有'
    # }
    # state = {
    #     1 : "intance_images/money_image.png"
    # }
    # save_game(state,'species_intance_enemy_pool.pkl','level/enemy pool')
    # state = load_game('switch_enemy_pool.pkl')
    # print(state)