import pyxel

import math
import random

pyxel.init(200,200)

ballxs = [random.randint(0,199) for x in range(3)] # starting pos in x-direction
ballys = [0,0,0]
angles = [math.radians(random.randint(30,150)) for a in range(3)]
vxs = [math.cos(angle) for angle in angles]    # starting vel x-direction
vys = [math.sin(angle) for angle in angles] # starting vel y-direction
padx = 100

score = 0
misses = 0
score_msg = f"score: {score}"
status = True

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)

def update():
    global ballxs, ballys, vxs, vys, padx, score, angles, misses, status
    if status:
        padx = pyxel.mouse_x
        for i in range(len(ballxs)):
            ballxs[i] += 2*vxs[i]
            ballys[i] += 2*vys[i]
            if ballxs[i] >= 200 or ballxs[i] <= 0:
                vxs[i] = -vxs[i]
            if ballys[i] >= 195 and (ballxs[i] >= padx-20 and ballxs[i] <= padx+20):
                pyxel.play(0,0)
                score += 1
                ballxs[i] = random.randint(0,199)
                ballys[i] = 0
                angle = math.radians(random.randint(30,150))
                vxs[i] = math.cos(angle)
                vys[i] = math.sin(angle)
            elif ballys[i] >= 200:
                misses += 1
                if misses == 10:
                    status = False
                    break
                ballxs[i] = random.randint(0,199)
                ballys[i] = 0
                angle = math.radians(random.randint(30,150))
                vxs[i] = math.cos(angle)
                vys[i] = math.sin(angle)


def draw():
    global ballxs, ballys, vxs, vys, padx, score, status
    pyxel.cls(7)
    if not status:
        pyxel.text(80, 90, "GAME OVER", 0)
    pyxel.text(5, 5, f"score: {score}", 0)
    pyxel.text(5, 15, f"misses: {misses}", 0)
    for i in range(0,len(ballxs)):
        pyxel.circ(ballxs[i], ballys[i], 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)


pyxel.run(update, draw)