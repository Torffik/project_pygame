import pygame
from copy import deepcopy
from random import randint

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            y_start = self.top + i * self.cell_size
            for j in range(self.width):
                x_start = self.left + j * self.cell_size
                size = (x_start, y_start, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, 'white', size, 1)

    def get_cell(self, mouse_pos):
        cell_x = ((mouse_pos[0] - self.left) // self.cell_size)
        cell_y = ((mouse_pos[1] - self.top) // self.cell_size)
        if (cell_x < 0 or cell_x > (self.width - 1)) or (cell_y < 0 or cell_y > (self.height - 1)):
            return 0
        else:
            a = (cell_x, cell_y)
            return a

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Морские бои ВПЕРЕД!!!')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    running = True
    minesweeper = Board(10, 10)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            minesweeper.render()
        pygame.display.flip()
    pygame.quit()
