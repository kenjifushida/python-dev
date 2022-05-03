import pyxel

import math
import random

pyxel.init(200,200)

ballx = random.randint(0,199)
bally = 0
angle = math.radians(random.randint(30,150))
vx = math.cos(angle)    # starting position x-direction
vy = math.sin(angle)  # starting position y-direction
speed = 1
padx = 100
score = 0

def update():
    global ballx, bally, vx, vy, padx, score, angle, speed
    ballx += speed*vx
    bally += speed*vy
    if ballx >= 200 or ballx <= 0:
        vx = -vx
    if bally >= 195 and (ballx >= padx-20 and ballx <= padx+20):
        score += 1
        speed += 0.5
        ballx = 100
        bally = 0
    elif bally >= 200:
        ballx = 100
        bally = 0
    padx = pyxel.mouse_x


def draw():
    global ballx, bally, vx, vy, padx, score
    pyxel.cls(7)
    pyxel.text(5, 5, f"score: {score}", 0)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)

pyxel.run(update, draw)