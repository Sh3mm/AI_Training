from enum import Enum


class Dir(Enum):
    R = 0
    L = 1
    U = 2
    D = 3
    C = 4


class Vision:
    def __init__(self, L=0, R=0, D=0, U=0):
        self.crash = False
        self.L = L
        self.R = R
        self.D = D
        self.U = U


init_game = False
vec_in = [Dir.R, Dir.D]
vec_out = [Vision(), Vision()]
