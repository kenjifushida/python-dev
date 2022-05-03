import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)

x1 = 0
y1 = 0

x2 = 0
y2 = 0

keypress = 0

def update():
    global x1, y1, x2, y2, keypress
    if pyxel.btnp(pyxel.KEY_SPACE) and keypress == 0:
        x1 = pyxel.mouse_x
        y1 = pyxel.mouse_y
        keypress += 1
    elif pyxel.btnp(pyxel.KEY_SPACE) and keypress == 1:
        x2 = pyxel.mouse_x
        y2 = pyxel.mouse_y
        keypress += 1
    elif pyxel.btnp(pyxel.KEY_SPACE) and keypress == 2:
        x1 = pyxel.mouse_x
        y1 = pyxel.mouse_y
        keypress = 1
        
    if keypress == 1:
        x2 = pyxel.mouse_x
        y2 = pyxel.mouse_y

def draw():
    global x1, y1, x2, y2
    pyxel.cls(7)
    pyxel.line(x1, y1, x2, y2, 0)

pyxel.run(update, draw)