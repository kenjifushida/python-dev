import pyxel

pyxel.init(200,200)

a = 200

def update():
  global a
  while 0< a <= 200:
    a -= 1
  if a == 0:
    while a < 200:
      a += 1

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a ,a ,10 ,0 )

pyxel.run(update, draw)