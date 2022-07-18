import pygame as pg
from pieces import *
from tile import Inventory_Tile
from Setup import *


class Turn_Panel:
    def __init__(self):
        outline_width = 0.25 * width
        outline_height = 0.05 * height

        self.inner_left = 5
        self.inner_top = 5
        self.inner_width = outline_width - 10
        self.inner_height = outline_height - 10

        self.back_panel = pg.Rect(0, 0, outline_width, outline_height)

    def draw(self, background, turn):
        FONT = pg.font.SysFont('Times New Norman', 25)
        if turn % 2 == 1:  # turn starts at 1
            font = FONT.render('Player 1:', True, black1)
        else:
            font = FONT.render('Player 2:', True, black1)

        title_rect = font.get_rect(center=(self.inner_left + self.inner_width * (2 / 5), self.inner_top + self.inner_height / 2))
        pg.draw.rect(background, yellow1, self.back_panel)

        if turn % 2 == 1:
            pg.draw.circle(background, white2, (self.inner_left + self.inner_width * (7 / 8), self.inner_top + self.inner_height / 2), 13)
        else:
            pg.draw.circle(background, black2, (self.inner_left + self.inner_width * (7 / 8), self.inner_top + self.inner_height / 2), 13)

        background.blit(font, title_rect)
        pg.display.flip()
