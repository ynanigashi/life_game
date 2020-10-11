import sys
import random
import math
import os
import getopt
import pygame
from pygame.locals import *


# config
cell_cols = 10
cell_rows = 20




class Game:
    direction = 1

    border = 1
    bg_color = (30, 30, 30)
    cell_size = 40

    def __init__(self):
        pygame.display.set_caption('tetro')
        self.screen = pygame.display.set_mode((480, 840))
        pygame.init()
        pygame.key.set_repeat(200,100)
        self.clock = pygame.time.Clock()
        # self.mino = self.create_mino()
        self.msec = 0
        self.interval = 1000

    def _draw_cell(self, color, cx, cy):
        px = cx * self.cell_size
        py = cy * self.cell_size
        pygame.draw.rect(self.screen, self.bg_color, (px, py, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, color, (
            px + self.border, py + self.border,
            self.cell_size-self.border, self.cell_size-self.border))


    def display(self):
        progress = (self.msec % self.interval) / self.interval
        # clear
        self.screen.fill(self.bg_color)
        # drawing
        for x in range(0, cell_rows):
            for y in range(0, 1):
                self._draw_cell((30, 30, 30), x, y)
        # update
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
            # display and wait
            self.msec += self.display()

if __name__ == '__main__':
    game = Game()
    game.gameloop()