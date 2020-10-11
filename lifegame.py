import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *


# config
cell_cols = 50
cell_rows = 50
cell_size = 20

class Game:
    direction = 1
    border = 1
    bg_color = (230, 230, 230)
    fg_color = (30, 30, 30)

    def __init__(self):
        pygame.display.set_caption('life game')
        self.screen = pygame.display.set_mode((cell_cols * cell_size, cell_rows * cell_size))
        pygame.init()
        pygame.key.set_repeat(200,100)
        self.clock = pygame.time.Clock()
        self.interval = 1000
        self.matrix = [[0 for _ in range(cell_cols)] for _ in range(cell_rows)]

    def _draw_cell(self, color, cx, cy):
        px = cx * cell_size
        py = cy * cell_size
        if self.matrix[cx][cy] == 1: state = 0
        else: state = 1
        pygame.draw.rect(self.screen, self.fg_color, (px, py, cell_size, cell_size), state)

    def display(self):
        # clear
        self.screen.fill(self.bg_color)
        # drawing
        for i in range(cell_cols):
            for j in range(cell_rows):
                self._draw_cell(self.fg_color, i, j)
        pygame.display.flip()
        return self.clock.tick(120)

    def gameover(self):
        self.__init__()

    def gameloop(self):
        pressed = False
        while 1:
            # # handle input
            for event in pygame.event.get():
                if event.type == QUIT: return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: return
                elif event.type == MOUSEBUTTONDOWN:
                    pressed = True
                elif event.type == MOUSEBUTTONUP:
                    pressed = False

            if pressed:
                x, y = pygame.mouse.get_pos()
                x //= cell_size
                y //= cell_size
                self.matrix[x][y] = 1
                print(x, y)
            # display and wait
            self.display()

if __name__ == '__main__':
    game = Game()
    game.gameloop()
