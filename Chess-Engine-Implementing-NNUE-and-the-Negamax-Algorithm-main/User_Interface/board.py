import pygame as game

BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

class board():
    
    def loadImages():
        """
        Initialize a global directory of images.
        This will be called exactly once in the main.
        """
        pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
        for piece in pieces:
            IMAGES[piece] = game.transform.scale(game.image.load("Assets\images\\" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

    def drawBoard(screen):
        """
        Draw the squares on the board.
        The top left square is always light.
        """

        screen = game.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
        global colors
        colors = [game.Color("white"), game.Color("gray")]
        for row in range(DIMENSION):
            for column in range(DIMENSION):
                color = colors[((row + column) % 2)]
                game.draw.rect(screen, color, game.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawPieces(screen, board):
        """
        Draw the pieces on the board using the current game_state.board
        """
        for row in range(DIMENSION):
            for column in range(DIMENSION):
                piece = board[row][column]
                if piece != "--":
                    screen.blit(IMAGES[piece], game.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def init_board(self):
        game.init()
        screen = game.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
        clock = game.time.Clock()
        screen.fill(game.Color("white"))