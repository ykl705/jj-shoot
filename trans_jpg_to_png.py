from PIL import Image

def trans():
    jpg_img = Image.open('images/enemy/ren3.jpg')
    jpg_img.save('images/ren3.png','PNG')

trans()