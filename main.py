"""
This is the main file that calls and makes the other components of the engine work.

Main driver file
Handling user input
"""
import pygame as game
import sys
from multiprocessing import Process, Queue

from User_Interface.board import board

def main():
    
    board.init_board()

    

