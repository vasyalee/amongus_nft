def draw_body(im, color):
    x_ax = 114
    y_ax = 76
    for i in range(28):
        if x_ax == 266:
            x_ax = 114
            y_ax += 38
            for x in range(x_ax, x_ax + 38):
                for y in range(y_ax, y_ax + 38):
                    im.putpixel((x, y), color)
        else:
            for x in range(x_ax, x_ax + 38):
                for y in range(y_ax, y_ax + 38):
                    im.putpixel((x, y), color)
        x_ax += 38

def draw_legs(im, color):
    for i in range(2):
        x_ax = 76
        y_ax = 304
        for x in range(x_ax, x_ax + 38):
            for y in range(y_ax, y_ax + 38):
                im.putpixel((x, y), color)
        x_ax = 190
        y_ax = 304
        for x in range(x_ax, x_ax + 38):
            for y in range(y_ax, y_ax + 38):
                im.putpixel((x, y), color)

def draw_between_legs(im):
    x_ax = 152
    y_ax = 304
    for x in range(x_ax, x_ax + 38):
        for y in range(y_ax, y_ax + 38):
            im.putpixel((x, y), (192, 192, 192))
    x_ax = 152
    y_ax = 266
    for x in range(x_ax, x_ax + 38):
        for y in range(y_ax, y_ax + 38):
            im.putpixel((x, y), (192, 192, 192))
    x_ax += 38
    for x in range(x_ax, x_ax + 38):
        for y in range(y_ax, y_ax + 38):
            im.putpixel((x, y), (192, 192, 192))

def draw_eyes(im, color):
    x_ax = 152
    y_ax = 114
    for x in range(x_ax, x_ax + 38):
        for y in range(y_ax, y_ax + 38):
            im.putpixel((x, y), color)
    x_ax += 38
    for x in range(x_ax, x_ax + 38):
        for y in range(y_ax, y_ax + 38):
            im.putpixel((x, y), color)

def draw_backpack(im, color):
    x_ax = 266
    y_ax = 114
    for i in range(3):
        if x_ax == 304:
            x_ax = 266
            y_ax += 38
            for x in range(x_ax, x_ax + 38):
                for y in range(y_ax, y_ax + 38):
                    im.putpixel((x, y), color)
        else:
            for x in range(x_ax, x_ax + 38):
                for y in range(y_ax, y_ax + 38):
                    im.putpixel((x, y), color)
        x_ax += 38

def make_body(im, body_color, val):
    draw_body(im, body_color)
    draw_legs(im, body_color)
    draw_between_legs(im)
    draw_eyes(im, (135, 206, 235))
    draw_backpack(im, body_color)