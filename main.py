"""
This is the main file that calls and makes the other components of the engine work.

Main driver file
Handling user input
"""
import pygame as game
import sys
from multiprocessing import Process, Queue

BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = game.transform.scale(game.image.load("D:\singh\Desktop\chess-engine-master\chess\images\\" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    """
    Main driver of the code.
    Handles the user input and updates the graphics.
    """
    game.init()
    screen = game.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = game.time.Clock()
    screen.fill(game.Color("white"))
    