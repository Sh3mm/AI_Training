import pygame
from math import sqrt
from Communication import Dir, Vision
from GamePart.Wall import Wall


class DEFAULT_VAL:
    x = 20
    y = 20
    width = 20
    height = 20
    speed = 1
    color = {"r": 255, "g": 255, "b": 255}


class Car:
    def __init__(self):
        self.x = DEFAULT_VAL.x
        self.y = DEFAULT_VAL.y

        self.width = DEFAULT_VAL.width
        self.height = DEFAULT_VAL.height

        self.speed = DEFAULT_VAL.speed
        self. vision = Vision()

        self.color = DEFAULT_VAL.color.copy()

    def add_in_game(self, win) -> None:
        pygame.draw.rect(
            win,
            (self.color["r"], self.color["g"], self.color["b"]),
            (self.x, self.y, self.width, self.height)
        )

    def move(self, direction: Dir) -> None:
        if direction == Dir.L: self.x -= self.speed
        if direction == Dir.R: self.x += self.speed
        if direction == Dir.U: self.y -= self.speed
        if direction == Dir.D: self.y += self.speed

    def collision(self, walls: [Wall]) -> bool:
        for wall in walls:
            if wall.in_zone(self.x, self.y) or\
                    wall.in_zone(self.x + self.width, self.y) or\
                    wall.in_zone(self.x, self.y + self.height) or\
                    wall.in_zone(self.x + self.width, self.y + self.height):
                self.color["g"] = 0
                self.color["b"] = 0
                return True
        return False

    def get_vision(self, walls: [Wall]) -> Vision:
        vision = Vision()
        center = (self.x + self.width/2, self.y + self.height/2)

        for wall in walls:
            wpoints = wall.get_points()

            point = self.find_closest_point(center, wpoints)
            if point is not None:
                self.set_vision(center, point, vision)

        self.vision = vision
        return vision

    @staticmethod
    def find_closest_point(c: [int, int], w: [[int, int]]) -> [int, int]:
        w.sort(key=lambda l: sqrt((l[0] - c[0]) ** 2 + (l[1] - c[1]) ** 2))

        projection = []
        for i in range(1, 3):
            x1, y1 = w[i]
            x2, y2 = w[0]
            x3, y3 = c
            dx, dy = x2 - x1, y2 - y1
            det = dx * dx + dy * dy
            a = (dy * (y3 - y1) + dx * (x3 - x1)) / det

            projection.append([x1+a*dx, y1+a*dy])

        for i in range(1, 3):
            sx = w[0][0] if w[0][0] < w[i][0] else w[i][0]
            bx = w[i][0] if w[0][0] < w[i][0] else w[0][0]

            sy = w[0][1] if w[0][1] < w[i][1] else w[i][1]
            by = w[i][1] if w[0][1] < w[i][1] else w[0][1]

            if sx <= projection[i-1][0] <= bx and sy <= projection[i-1][1] <= by:
                return projection[i-1]

    @staticmethod
    def set_vision(center: [int, int], point: [int, int], vision: Vision) -> None:

        if point[0] == center[0]:  # Right and left [0] == x axis
            if point[1] < center[1] and (center[1] - point[1] < vision.L or vision.L == 0):  # Left
                vision.L = center[1] - point[1]

            if point[1] > center[1] and (point[1] - center[1] < vision.R or vision.R == 0):  # Right
                vision.R = point[1] - center[1]

        if point[1] == center[1]:  # Up and Down [1] == y axis
            if point[0] < center[0] and (center[0] - point[0] < vision.U or vision.U == 0):  # Left
                vision.U = center[0] - point[0]

            if point[0] > center[0] and (point[0] - center[0] < vision.D or vision.D == 0):  # Right
                vision.D = point[0] - center[0]
