import time
import save_loader
from tqdm import tqdm



print('Now Resetting Archive...')

print('\n')

print('Now Resetting Save...')

list = save_loader.load_game('save.pkl')
for i in tqdm(range(0, 5)):
    list[i] = 0
    time.sleep(0.5)
save_loader.save_game(list, 'save.pkl')

print('\n')

print('Now Resetting Data...')

list = save_loader.load_game('data.pkl')
for i in tqdm(range(0, 6)):
    list[i] = 0
    time.sleep(0.5)
save_loader.save_game(list, 'data.pkl')




list = save_loader.load_game('date.pkl')
list[0] = ' '
save_loader.save_game(list,'date.pkl')

print('\n')

print('Finished!!\n')

input("Press Enter to exit...")