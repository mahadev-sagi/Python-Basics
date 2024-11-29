#version-2 with two player game and restarting


import pygame, sys
from constants import *
from tictactoe import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


chip_font = pygame.font.Font(None, CHIP_FONT)


game_over_font = pygame.font.Font(None, GAME_OVER_FONT)


board = initialize_board()
# board[2][1] = 'x'
# board[0][0] = 'o'
player = 1
chip = 'x'
game_over = False
winner = 0


def draw_grid():
   #draw horizontal lines
   for i in range(1, BOARD_ROWS):
       pygame.draw.line(
           screen,
           LINE_COLOR,
           (0, i*SQUARE_SIZE),
           (WIDTH, i*SQUARE_SIZE),
           LINE_WIDTH
       )


   for i in range(1, BOARD_COLS):
       pygame.draw.line(
           screen,
           LINE_COLOR,
           (i*SQUARE_SIZE, 0),
           (i*SQUARE_SIZE, HEIGHT),
           LINE_WIDTH
       )


def draw_chips():
   chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
   chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)


   for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
           if board[row][col] == "x":
               chip_x_rect = chip_x_surf.get_rect(center=(col*SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2))
               screen.blit(chip_x_surf, chip_x_rect)
           elif board[row][col] == "o":
               chip_x_rect = chip_o_surf.get_rect(center=(col*SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2))
               screen.blit(chip_o_surf, chip_x_rect)


def draw_game_over():
   screen.fill(BG_COLOR)
   game_over_font = pygame.font.Font(None, GAME_OVER_FONT)


   if winner!=0:
       end_text = f"Player {winner} wins!"
   else:
       end_text = "No one wins"


   end_surf = game_over_font.render(end_text, 0, LINE_COLOR)
   end_rect = end_surf.get_rect(center = (WIDTH // 2, HEIGHT//2-50))
   screen.blit(end_surf, end_rect)


   restart_text = "Press r to restart the game"


   restart_surf = game_over_font.render(restart_text, 0, LINE_COLOR)
   restart_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
   screen.blit(restart_surf, restart_rect)






screen.fill(BG_COLOR)
draw_grid()




while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
           x, y = event.pos
           row = y // SQUARE_SIZE
           col = x // SQUARE_SIZE
           # print(row, col)
           # print(x, y)
           if available_square(board, row, col):
               mark_square(board, row, col, chip)
               if check_if_winner(board, chip):
                   game_over = True
                   winner = player
               else:
                   if board_is_full(board):
                       game_over = True
                       winner = 0 #indicates tie


               #alternate players
               player = 2 if player == 1 else 1
               chip = 'o' if chip == 'x' else 'x'


           draw_chips()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_r and game_over:
               #restarting the game
               screen.fill(BG_COLOR)
               draw_grid()
               player = 1
               chip = 'x'
               game_over = False
               winner = 0
               board = initialize_board()


   if game_over:
       pygame.display.update()
       pygame.time.delay(1000)
       draw_game_over()




   pygame.display.update()

