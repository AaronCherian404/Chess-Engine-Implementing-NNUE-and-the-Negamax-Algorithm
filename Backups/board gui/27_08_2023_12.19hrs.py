import pygame

# Initialize the pygame library
pygame.init()

# Create a chess board surface
chess_board_surface = pygame.Surface((500, 500))

# Draw the chess board
for i in range(8):
  for j in range(8):
    if (i+j) % 2 == 0:
      pygame.draw.rect(chess_board_surface, (255, 255, 255), (i*50, j*50, 50, 50))
    else:
      pygame.draw.rect(chess_board_surface, (0, 0, 0), (i*50, j*50, 50, 50))

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
    #   sys.exit()