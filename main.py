import pygame
from checkers.constants import WHITE, WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game
from minimax.algorithm import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minimax')

def getRowColFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(60)

        if game.turn == WHITE:
            value,newBoard = minimax(game.getBoard(),3,WHITE,game) 
            game.aiMove(newBoard)          

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getRowColFromMouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()