import pygame
import os

# Initialize the pygame library
pygame.init()

# Create a chess board surface
chess_board_surface = pygame.Surface((500, 500))

# Load piece images
image_path = 'D:\\Workspaces\\CHESS\\Chess-Engine-Implementing-NNUE-and-the-Negamax-Algorithm\\Assets\\images\\'

piece_images = {
    'wp': pygame.image.load(os.path.join(image_path, 'wp.png')),
    'wr': pygame.image.load(os.path.join(image_path, 'wR.png')),
    'wn': pygame.image.load(os.path.join(image_path, 'wN.png')),
    'wb': pygame.image.load(os.path.join(image_path, 'wB.png')),
    'wq': pygame.image.load(os.path.join(image_path, 'wQ.png')),
    'wk': pygame.image.load(os.path.join(image_path, 'wK.png')),
    'bp': pygame.image.load(os.path.join(image_path, 'bp.png')),
    'br': pygame.image.load(os.path.join(image_path, 'bR.png')),
    'bn': pygame.image.load(os.path.join(image_path, 'bN.png')),
    'bb': pygame.image.load(os.path.join(image_path, 'bB.png')),
    'bq': pygame.image.load(os.path.join(image_path, 'bQ.png')),
    'bk': pygame.image.load(os.path.join(image_path, 'bK.png')),
    # Add more piece images here for all pieces and colors
}

# Initial position of the pieces
initial_position = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    [None] * 8,  # Empty squares
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
]

# Draw the chess board and pieces
square_size = 50
for i in range(8):
    for j in range(8):
        color = (255, 255, 255) if (i + j) % 2 == 0 else (200, 200, 200)
        pygame.draw.rect(chess_board_surface, color, (i * square_size, j * square_size, square_size, square_size))

        # Render pieces on the board
        piece = initial_position[j][i]
        if piece is not None:
            piece_image = piece_images[piece]
            piece_rect = piece_image.get_rect()
            piece_rect.center = ((i + 0.5) * square_size, (j + 0.5) * square_size)
            chess_board_surface.blit(piece_image, piece_rect.topleft)

# Create a window to display the chess board
window = pygame.display.set_mode((500, 500))

# Display the chess board
window.blit(chess_board_surface, (0, 0))

# Update the display
pygame.display.update()

# Wait for the user to quit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
