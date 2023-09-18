from checkers.board import Board
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.minimax import minimax

FPS = 60

WHITE_DEPTH = 2
RED_DEPTH = 4

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def getRowColFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    turn = 0
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, newBoard = minimax(game.getBoard(), WHITE_DEPTH, True)
            if game.getBoard() == newBoard:
                turn += 1
            game.aiMove(newBoard)

        if turn > 10 or turn <-10:
            pygame.time.delay(10000)
            if turn > 0:
                print('There is no move for WHITE player!')
            else:
                print('There is no move for RED player!')
            if game.getBoard().redLeft > game.getBoard().whiteLeft:
                print('The RED Player wins!')
            elif game.getBoard().redLeft < game.getBoard().whiteLeft:
                print('The WHITE Player wins!')
            else:
                print('Tie!')
            run = False
        
        if game.winner() != None:
            print(game.winner())
            run = False

        if game.turn == RED:
            value, newBoard = minimax(game.getBoard(), RED_DEPTH, False)
            if game.getBoard() == newBoard:
                turn -= 1
            game.aiMove(newBoard)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.update()
        # pygame.time.delay(500)
    
    pygame.quit()