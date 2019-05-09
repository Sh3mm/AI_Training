from threading import Thread
import Communication as Com
from GamePart.RaceGame import Game


if __name__ == "__main__":
    n_bot = int(input("Enter the number of bot per cycle: "))

    Com.vec_in = [Com.Dir.C for _ in range(n_bot)]
    Com.vec_out = [Com.Vision() for _ in range(n_bot)]

    game = Game(n_bot)

    t1 = Thread(target=game.run)
    t2 = Thread()  # todo: add the bot part

    t1.join()
    t2.join()
