import pyxel
import random

pyxel.init(200,200, scale=2)
pyxel.mouse(True)

xs = []
ys = []
rs = []
cs = []

def update():
    global xs, ys, rs, cs
    if pyxel.btnp(pyxel.KEY_SPACE):
        xs.append(pyxel.mouse_x)
        ys.append(pyxel.mouse_y)
        rs.append(random.randint(5,20))
        cs.append(random.randint(0,15))

def draw():
    global xs, ys, rs, cs
    pyxel.cls(7)
    for i in range(0, len(xs)):
        pyxel.circ(xs[i], ys[i], rs[i], cs[i])

pyxel.run(update, draw)