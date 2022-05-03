import pyxel

import math
import random

pyxel.init(200,200)

ballxs = [random.randint(0,199)] # starting pos in x-direction
ballys = [0]
angle = math.radians(random.randint(30,150))
vxs = [math.cos(angle)]    # starting vel x-direction
vys = [math.sin(angle)] # starting vel y-direction
speed = 1
padx = 100

score = 0
misses = 0
score_msg = f"score: {score}"
status = True

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)

def update():
    global ballxs, ballys, vxs, vys, padx, score, angle, misses, status, speed
    if status:
        padx = pyxel.mouse_x
        for i in range(len(ballxs)):
            ballxs[i] += speed*vxs[i]
            ballys[i] += speed*vys[i]
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
                if score > 0 and score % 10 == 0:
                    ballxs.append(random.randint(0,199))
                    ballys.append(0)
                    angle = math.radians(random.randint(30,150))
                    vxs.append(math.cos(angle))
                    vys.append(math.sin(angle))
                    speed = 1
                    break
                speed += 0.5
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