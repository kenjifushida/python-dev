import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for b in range(10, 200, 20):
    for a in range(30, 200, 40):
        if (b-10) % 40 != 0 and (b-10) % 20 == 0:
            pyxel.circ(a, b, 10, 12)
        else:
            pyxel.circ(a, b, 10, 14)
for b in range(10, 200, 20):
    for a in range(10, 200, 40):
        if (b-10) % 40 != 0 and (b-10) % 20 == 0:
            pyxel.circ(a, b, 10, 14)
        else:
            pyxel.circ(a, b, 10, 12)
pyxel.show()