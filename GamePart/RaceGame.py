import pygame
import Communication as Com
from GamePart.Car import Car
from Communication import Dir
from GamePart.Wall import Wall


class Game:
    def __init__(self, n_car):
        pygame.init()
        pygame.display.set_caption("race game")
        outer_walls = [
            Wall(0, 0, 500, 10),
            Wall(0, 0, 10, 500),
            Wall(490, 0, 10, 500),
            Wall(0, 490, 500, 10),
        ]
        inner_walls = [
            Wall(50, 50, 390, 10),
            Wall(50, 50, 10, 390),
            Wall(440, 50, 10, 400),
            Wall(50, 440, 400, 10),
        ]

        self.win = pygame.display.set_mode((500, 500))
        self.cars = [Car() for x in range(n_car)]
        self.walls = outer_walls + inner_walls

    def reset(self):
        self.cars = [Car() for _ in range(len(self.cars))]

    def press(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if Com.init_game:
            Com.init_game = not Com.init_game
            self.reset()

        for i in range(len(self.cars)):
            if not self.cars[i].collision(self.walls):
                self.cars[i].move(Com.vec_in[i])
                Com.vec_out[i] = self.cars[i].get_vision(self.walls)

            else:
                Com.vec_out[i] = False

            Com.vec_in[i] = Dir.C

        return True

    def run(self):

        run = True
        while run:
            pygame.time.delay(20)

            run = self.press()

            self.win.fill((0, 0, 0))
            [car.add_in_game(self.win) for car in self.cars]
            [wall.add_in_game(self.win) for wall in self.walls]
            pygame.display.update()

        pygame.quit()
