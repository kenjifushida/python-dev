import pyxel

import math
import random


class Ball:
    speed = 1

    def __init__(self):
        self.restart()

    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
        if self.x >= 200 or self.x <= 0:
                self.vx = -self.vx
        if self.y >= 200:
            self.restart()
            return True
        return False
        
    def restart(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)

class Pad:
    def __init__(self):
        self.x = pyxel.mouse_x

    def catch(self, b):
        if b.y >= 195 and (b.x >= self.x-20 and b.x <= self.x+20):
                pyxel.play(0,0)
                b.restart()
                return True


pyxel.init(200,200)

ball1 = Ball() # first instance of ball class
balls = [ball1]
pad = Pad()

score = 0
misses = 0
score_msg = f"score: {score}"
status = True

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)

def update():
    global score, misses, status
    if status:
        pad.x = pyxel.mouse_x
        for b in balls:
            result = b.move()
            pad_catch = pad.catch(b)
            if pad_catch:
                score += 1
                if score > 0 and score % 10 == 0:
                    new_ball = Ball()
                    balls.append(new_ball)
                    Ball.speed = 1
                    break
                Ball.speed += 1
            elif result:
                misses += 1
                if misses == 10:
                    status = False
                    break


def draw():
    global score, status
    pyxel.cls(7)
    if not status:
        pyxel.text(80, 90, "GAME OVER", 0)
    pyxel.text(5, 5, f"score: {score}", 0)
    pyxel.text(5, 15, f"misses: {misses}", 0)
    for b in balls:
        pyxel.circ(b.x, b.y, 10, 6)
    pyxel.rect(pad.x-20, 195, 40, 5, 14)


pyxel.run(update, draw)