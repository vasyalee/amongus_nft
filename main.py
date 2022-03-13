from PIL import Image, ImageColor
from secrets import *
from draw import *
from dict_generator import *

def get_key(val):
    for key, value in dictionary.items():
         if val == value:
             return key


im = Image.new(mode="RGBA", size=(380,380), color=(192, 192, 192))
dictionary = create_dict()
name = 0
for key, value in dictionary.items():
    body_color = dictionary.get(key)
    val = body_color
    body_color = body_color.split(',')
    last_item = body_color[2][:-1]
    body_color.remove(body_color[2])
    body_color.append(last_item)
    body_color = [int(num) for num in body_color]
    body_color = tuple(body_color)

    make_body(im, body_color, val)
    name = get_key(val)

    im.save(f'{name} amogus.png')