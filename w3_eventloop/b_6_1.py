import pyxel
import math

pyxel.init(200, 200)

a = 0

def update():
    global a
    # if a >= 200:
    #     a = 0
    # a += 1

    if pyxel.btnp(pyxel.KEY_SPACE):
        a+=math.radians(1)

def draw():
    global a
    pyxel.cls(7)
    # pyxel.circ(a, a, 10, 0)
    pyxel.line(100, 100,100 + 5*math.cos(a),100 + 5*math.sin(-a), 0)
    
pyxel.run(update, draw)