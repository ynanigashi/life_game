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
        self.interval = 100
        self.matrix = [[0 for _ in range(cell_cols)] for _ in range(cell_rows)]
        self.msec = 0

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
        return

    def gameover(self):
        self.__init__()

    def count_neighbor_cells(self, x, y):
        cells = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        alive = 0
        for rx, ry in cells:
            if 0 <= x + rx < cell_cols and 0 <= y + ry < cell_rows:
                if self.matrix[x + rx][y + ry] == 1:
                    alive += 1
        return alive

    def process_rules(self):
        matrix = [[0 for _ in range(cell_cols)] for _ in range(cell_rows)]
        for i in range(cell_cols):
            for j in range(cell_rows):
                alive = self.count_neighbor_cells(i, j)
                if alive <= 1 or alive >= 4:
                    matrix[i][j] = 0
                elif alive == 2:
                    matrix[i][j] = self.matrix[i][j]
                elif alive == 3:
                    matrix[i][j] = 1
        self.matrix = matrix
        print('rules')
        
    def gameloop(self):
        pressed = False
        pause = True
        while 1:
            # # handle input
            for event in pygame.event.get():
                if event.type == QUIT: return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: return
                    elif event.key == K_SPACE:
                        pause = not pause
                        
                elif event.type == MOUSEBUTTONDOWN:
                    pressed = True
                elif event.type == MOUSEBUTTONUP:
                    pressed = False

            if pressed:
                x, y = pygame.mouse.get_pos()
                x //= cell_size
                y //= cell_size
                buttons = pygame.mouse.get_pressed()
                if buttons[0]:
                    self.matrix[x][y] = 1
                elif buttons[2]:
                    self.matrix[x][y] = 0

            # display and wait
            self.display()
            if not pause:
                self.msec += self.clock.tick(60)
            if self.msec > self.interval:
                self.msec = 0
                self.process_rules()


if __name__ == '__main__':
    game = Game()
    game.gameloop()
