from tile import Inventory_Tile
from pieces import *
from Frame import Inventory_Frame
from Player_Panel import Turn_Panel
from Setup import *


class Game_State:
    def __init__(self, tiles=[], white_inventory=None, black_inventory=None):
        # state attributes
        self.running = True
        self.menu_loop = True
        self.main_loop = False
        self.end_loop = False
        self.play_new_game = False
        self.move_popup_loop = False

        # board
        white_inventory = Inventory_Frame((0, 158), 0, white=True)
        black_inventory = Inventory_Frame((440, 158), 1, white=False)
        self.board_tiles = tiles + white_inventory.Sections + black_inventory.Sections
        self.turn_panel = Turn_Panel()

        # action attributes
        self.clicked = False
        self.moving_piece = None
        self.turn = 1

        # other
        self.winner = None

    def start_game(self):
        self.menu_loop = False
        self.main_loop = True

    def end_game(self):
        self.main_loop = False
        self.end_loop = True

    def new_game(self):
        self.main_loop = True
        self.end_loop = False
        self.turn = 1

    def quit(self):
        self.running = False
        self.menu_loop = False
        self.main_loop = False
        self.end_loop = False

    def play_again(self):
        self.play_new_game = True
        self.quit()

    def open_popup(self):
        self.main_loop = False
        self.move_popup_loop = True

    def close_popup(self):
        self.main_loop = True
        self.move_popup_loop = False
        self.next_turn()

    def add_moving_piece(self, piece):
        self.moving_piece = piece

    def remove_moving_piece(self):
        self.moving_piece = None

    def click(self):
        self.clicked = True

    def unclick(self):
        self.clicked = False

    def add_tiles(self, tiles):
        self.tiles = self.board_tiles.extend(tiles)

    def next_turn(self):
        self.turn += 1

    def is_player_turn(self):
        if self.moving_piece.color == white1 and self.turn % 2 == 1:
            return True
        elif self.moving_piece.color == black1 and self.turn % 2 == 0:
            return True
        else:
            return False

    def get_tiles_with_pieces(self, include_inventory=False):
        tiles = []
        for tile in self.board_tiles:
            if include_inventory:
                if tile.has_pieces():
                    tiles.append(tile)
            elif tile.has_pieces() and type(tile) is not Inventory_Tile:
                tiles.append(tile)
        return tiles
