import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x=0
y=0

def update():
    global x, y
    if pyxel.btnp(pyxel.KEY_SPACE):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

def draw():
    global x, y
    pyxel.cls(7)
    pyxel.circ(x, y, 10, 0)

pyxel.run(update, draw)