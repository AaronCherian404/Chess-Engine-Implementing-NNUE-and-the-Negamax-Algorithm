import time
import math
from ctypes import *

# Load NNUE probe and init weights
nnue = cdll.LoadLibrary('./libnnueprobe.so')
nnue.nnue_init(b'./nn.nnue')

# Chess constants
PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = 1, 2, 3, 4, 5, 6
EMPTY = 13
A1, B1, C1, D1, E1, F1, G1, H1 = 91, 92, 93, 94, 95, 96, 97, 98
A2, H2 = 81, 88
A8, H8 = 21, 28
last_rank = [28, 27, 26, 25, 24, 23, 22, 21]
fen_pieces = 'PNBRQKpnbrqk'

# Directions for generating moves on a 10x12 board
N, E, S, W = -10, 1, 10, -1
directions = {
    PAWN: (N, N+N, N+W, N+E),
    KNIGHT: (N+N+E, E+N+E, E+S+E, S+S+E, S+S+W, W+S+W, W+N+W, N+N+W),
    BISHOP: (N+E, S+E, S+W, N+W),
    ROOK: (N, E, S, W),
    QUEEN: (N, E, S, W, N+E, S+E, S+W, N+W),
    KING: (N, E, S, W, N+E, S+E, S+W, N+W)
}
directions_isatt = {
    BISHOP + 6: (N+E, S+E, S+W, N+W),
    ROOK + 6: (N, E, S, W),
    KNIGHT + 6: (N+N+E, E+N+E, E+S+E, S+S+E, S+S+W, W+S+W, W+N+W, N+N+W),
    PAWN + 6: (N+E, N+W),
    KING + 6: (N, E, S, W, N+E, S+E, S+W, N+W)
}

# 10x12 board
mailbox = [
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
    -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
    -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
    -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
    -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
    -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
    -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
    -1,  0,  1,  2,  3, 4, 5, 6, 7, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
]
