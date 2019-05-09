import pygame


class Wall:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y

        self.width = w
        self.height = h

    def add_in_game(self, win) -> None:
        pygame.draw.rect(
            win,
            (0, 255, 255),
            (self.x, self.y, self.width, self.height),
        )

    def in_zone(self, x: int, y: int) -> bool:
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        return False

    def get_points(self) -> [[int, int]]:
        return [
            [self.x, self.y],
            [self.x + self.width, self.y],
            [self.x, self.y + self.height],
            [self.x + self.width, self.y + self.height]
        ]
