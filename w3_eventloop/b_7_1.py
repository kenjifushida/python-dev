import pyxel

pyxel.init(200, 200)

a = 0
direction = "right"

def update():
    global a, direction 
    if a >= 200:
        direction = "left"
    elif a <= 0:
        direction = "right"
    if pyxel.btnp(pyxel.KEY_SPACE):
        direction = "left" if direction == "right" else "right"
    if direction == "right":
        a += 1
    elif direction == "left":
        a-= 1


def draw():
    global a, direction
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)