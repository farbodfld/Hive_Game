import pygame as pg
from pieces import *
from tile import Inventory_Tile
from Setup import *


class Inventory_Frame:
    def __init__(self, pos, player, white=True):
        left = pos[0]
        top = height - pos[1]

        inventory_width = 0.5 * width
        inventory_height = 0.2 * height

        inner_left = left + 5
        inner_top = top + 5
        inner_width = inventory_width - 10
        inner_height = inventory_height - 10

        self.back_panel = pg.Rect(left, top, inventory_width, inventory_height)

        title_height = 0.1 * inner_height
        stock_height = 0.9 * inner_height
        stock_width = 0.2 * inner_width

        self.Section_rects = []
        self.Sections = []

        if white:
            self.color = white1
        else:
            self.color = black1

        count = 0
        while count < 5:
            self.Section_rects.append(pg.Rect(left + count * stock_width + 2, top + title_height + 2, stock_width - 4, stock_height - 4))

            if count == 0:
                Section_Position = (left + (count + 0.5) * stock_width, top + title_height + 0.5 * stock_height)
                self.Sections.append(Inventory_Tile(Section_Position, (99, 99), 20, self.color, piece=Queen(self.color)))

            if count == 1:
                for x in [0.33, 0.66]:
                    Section_Position = (left + (count + 0.5) * stock_width, top + title_height + x * stock_height)
                    self.Sections.append(Inventory_Tile(Section_Position, (99, 99), 20, self.color, piece=Beetle(self.color)))

            if count == 2:
                for x in [0.33, 0.66]:
                    Section_Position = (left + (count + 0.5) * stock_width, top + title_height + x * stock_height)
                    self.Sections.append(Inventory_Tile(Section_Position, (99, 99), 20, self.color, piece=Spider(self.color)))

            if count == 3:
                for x in [0.2, 0.5, 0.8]:
                    Section_Position = (left + (count + 0.5) * stock_width, top + title_height + x * stock_height)
                    self.Sections.append(Inventory_Tile(Section_Position, (99, 99), 20, self.color, piece=Grasshopper(self.color)))

            if count == 4:
                for x in [0.2, 0.5, 0.8]:
                    Section_Position = (left + (count + 0.5) * stock_width, top + title_height + x * stock_height)
                    self.Sections.append(Inventory_Tile(Section_Position, (99, 99), 20, self.color, piece=Ant(self.color)))

            count += 1

        for tile in self.Sections:
            for piece in tile.pieces:
                piece.update_pos(tile.coords)

        font = pg.font.SysFont('Times New Norman', 24)
        if player == 0:
            self.font = font.render('Player 1', True, white2)
        else:
            self.font = font.render('Player 2', True, white2)
        self.title_rect = self.font.get_rect(center=(inner_left + inner_width / 2, inner_top + title_height / 2))

    def draw(self, background, pos):
        pg.draw.rect(background, black2, self.back_panel)
        pg.draw.rect(background, panel, self.title_rect)

        for i in range(0, len(self.Section_rects)):
            pg.draw.rect(background, self.color, self.Section_rects[i])

        background.blit(self.font, self.title_rect)
        pg.display.flip()