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
        self.cell_size = 50
        self.one = False
        self.two = False
        self.three = False
        self.four = False

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for a in range(0, 4):
            font = pygame.font.Font(None, 20)
            text_x = self.left + (self.cell_size * 2) * a + 5
            text_y = self.height * (self.cell_size + 1) + self.top + 3
            if self.one:
                if a == 0:
                    text = font.render(str(a + 1), True, (255, 255, 255))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'white',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
                else:
                    text = font.render(str(a + 1), True, (100, 255, 100))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'green',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
            elif self.two:
                if a == 1:
                    text = font.render(str(a + 1), True, (255, 255, 255))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'white',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
                else:
                    text = font.render(str(a + 1), True, (100, 255, 100))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'green',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
            elif self.three:
                if a == 2:
                    text = font.render(str(a + 1), True, (255, 255, 255))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'white',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
                else:
                    text = font.render(str(a + 1), True, (100, 255, 100))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'green',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
            elif self.four:
                if a == 3:
                    text = font.render(str(a + 1), True, (255, 255, 255))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'white',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
                else:
                    text = font.render(str(a + 1), True, (100, 255, 100))
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, 'green',
                                     (self.left + (self.cell_size * 2) * a, self.height *
                                      (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                     1)
            else:
                text = font.render(str(a + 1), True, (100, 255, 100))
                screen.blit(text, (text_x, text_y))
                pygame.draw.rect(screen, 'green',
                                (self.left + (self.cell_size * 2) * a, self.height *
                                (self.cell_size + 1) + self.top, self.cell_size * 2, self.cell_size),
                                1)
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
            if self.if_button(mouse_pos):
                a = self.button_number(mouse_pos)
                if a == 1:
                    self.one = True
                    self.two = False
                    self.three = False
                    self.four = False
                elif a == 2:
                    self.one = False
                    self.two = True
                    self.three = False
                    self.four = False
                elif a == 3:
                    self.one = False
                    self.two = False
                    self.three = True
                    self.four = False
                elif a == 4:
                    self.one = False
                    self.two = False
                    self.three = False
                    self.four = True
        else:
            a = (cell_x, cell_y)
            return a

    def if_button(self, pos):
        x = pos[0]
        y = pos[1]
        start_x = self.left
        start_y = self.height * (self.cell_size + 1) + self.top
        end_x = self.left + (self.cell_size * 2) * 4
        end_y = self.height * (self.cell_size + 1) + self.top + self.cell_size
        if start_x < x < end_x and start_y < y < end_y:
            return True
        else:
            return False

    def button_number(self, pos):
        x = pos[0]
        if self.left < x < self.left + (self.cell_size * 2):
            return 1
        elif self.left + (self.cell_size * 2) < x < self.left + (self.cell_size * 2) * 2:
            return 2
        elif self.left + (self.cell_size * 2) * 2 < x < self.left + (self.cell_size * 2) * 3:
            return 3
        elif self.left + (self.cell_size * 2) * 3 < x < self.left + (self.cell_size * 2) * 4:
            return 4

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Морские бои')
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    running = True
    battle = Board(6, 6)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                battle.get_cell(event.pos)
            battle.render()
        pygame.display.flip()
    pygame.quit()
