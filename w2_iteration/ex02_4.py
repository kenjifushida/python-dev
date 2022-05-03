import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for b in range(10, 200, 40):
    for a in range(30, 200, 40):
        pyxel.circ(a, b, 10, 14)
for b in range(30, 200, 40):
    for a in range(10, 200, 40):
        pyxel.circ(a, b, 10, 14)
for b in range(10, 200, 40):
    for a in range(10, 200, 40):
        pyxel.circ(a, b, 10, 12)
for b in range(30, 200, 40):
    for a in range(30, 200, 40):
        pyxel.circ(a, b, 10, 12)
pyxel.show()