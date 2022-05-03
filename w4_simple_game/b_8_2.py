import pyxel

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866    # cos 60 degree
vy = 0.5  # sin 60 degree
padx = 100
speed = 1

def update():
    global ballx, bally, vx, vy, padx, speed
    ballx += speed*vx
    bally += speed*vy
    if ballx >= 200:
        vx = -0.866
    elif ballx <= 0:
        vx = 0.866
    if bally >= 200:
        ballx = 100
        bally = 0
        speed += 1
    padx = pyxel.mouse_x

def draw():
    global ballx, bally, vx, vy, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)

pyxel.run(update, draw)