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


class App:
    def __init__(self):
        pyxel.init(200,200)

        self.balls = [Ball()]
        self.pad = Pad()
        self.score = 0
        self.misses = 0
        self.status = True

        pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.status:
            self.pad.x = pyxel.mouse_x
            for b in self.balls:
                result = b.move()
                pad_catch = self.pad.catch(b)
                if pad_catch:
                    self.score += 1
                    if self.score > 0 and self.score % 10 == 0:
                        new_ball = Ball()
                        self.balls.append(new_ball)
                        Ball.speed = 1
                        break
                    Ball.speed += 1
                elif result:
                    self.misses += 1
                    if self.misses == 10:
                        self.status = False
                        break

    def draw(self):
        pyxel.cls(7)
        if not self.status:
            pyxel.text(80, 90, "GAME OVER", 0)
        pyxel.text(5, 5, f"score: {self.score}", 0)
        pyxel.text(5, 15, f"misses: {self.misses}", 0)
        for b in self.balls:
            pyxel.circ(b.x, b.y, 10, 6)
        pyxel.rect(self.pad.x-20, 195, 40, 5, 14)


App()