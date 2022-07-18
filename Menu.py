import pygame as pg
import webbrowser
from Setup import *

START = 'START'
OPTIONS = 'OPTIONS'
NEWGAME = 'NEW GAME'
QUIT = 'QUIT'


class StartButton:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect
        self.color = black2

    def run_if_clicked(self, pos, state):
        if self.rect.collidepoint(pos):
            if self.text == START:
                state.start_game()
                return

    def draw(self, background):
        FONT = pg.font.SysFont('Times New Norman', 45)
        font = FONT.render(self.text, True, orange)

        pg.draw.rect(background, self.color, self.rect)
        background.blit(font, self.rect)


def start_menu(screen, state, event):
    button_width = 0.2 * width
    button_height = 0.1 * height
    button_pos = 0.5 * width - 0.5 * button_width

    rect1 = pg.Rect(button_pos, 3 / 9 * height, button_width, button_height)
    buttons = [StartButton(START, rect1)]

    if event.type == pg.MOUSEBUTTONDOWN:
        for button in buttons:
            button.run_if_clicked(event.pos, state)
    screen.fill(violet1)
    for button in buttons:
        button.draw(screen)
    pg.display.flip()


class EndButton:
    def __init__(self, text, pos):
        self.text = text

        font = pg.font.SysFont('Times New Norman', 90)
        self.FONT = font.render(self.text, True, purple)
        self.FONT.set_alpha(250)
        self.font_rect = self.FONT.get_rect(center=pos)

    def run_if_clicked(self, pos, state):
        if self.font_rect.collidepoint(pos):
            if self.text == NEWGAME:
                state.play_again()
                return
            elif self.text == QUIT:
                state.quit()
                return

    def draw(self, background):
        background.blit(self.FONT, self.font_rect)


def end_menu(screen, state, event):
    clear_surface = pg.Surface((width, height))
    clear_surface.set_alpha(5)
    clear_surface.fill(white2)
    buttons = [EndButton(NEWGAME, (width * 0.5, height * 0.5)),
               EndButton(QUIT, (width * 0.5, 0.65 * height))]

    title_font = pg.font.SysFont('Times New Norman', 120)

    if state.winner == white1:
        wins = title_font.render('White Wins!', True, purple)
    elif state.winner == black1:
        wins = title_font.render('Black Wins!', True, purple)
    else:
        wins = title_font.render('Draw', True, purple)
    wins.set_alpha(250)
    wins_rect = wins.get_rect(center=(width / 2, height / 8))

    if event.type == pg.MOUSEBUTTONDOWN:
        for button in buttons:
            button.run_if_clicked(event.pos, state)

    for button in buttons:
        button.draw(clear_surface)

    clear_surface.blit(wins, wins_rect)
    screen.blit(clear_surface, (0, 0))
    pg.display.flip()


def no_move_popup(screen, surface, state, event,):
    window_width = width / 2
    window_height = height / 3

    clear_surface = pg.Surface((window_width, window_height))
    clear_surface.set_alpha(5)
    clear_surface.fill(CLEAR)

    popup_font = pg.font.SysFont('Times New Norman', 32)

    if state.turn % 2 == 1:
        no_move = popup_font.render('White has no moves', True, purple)
        turn_skipped = popup_font.render('White turn is skipped', True, purple)
    else:
        no_move = popup_font.render('Black has no moves,', True, purple)
        turn_skipped = popup_font.render('Black turn is skipped', True, purple)
    close = popup_font.render('Press the space bar to close this message', True, purple)

    close.set_alpha(250)
    no_move.set_alpha(250)
    turn_skipped.set_alpha(250)

    close_rect = close.get_rect(center=(window_width / 2, window_height / 2 + window_height / 4))
    no_move_rect = no_move.get_rect(center=(window_width / 2, window_height / 2 - window_height / 3))
    turn_skipped_rect = turn_skipped.get_rect(center=(window_width * 0.5, window_height * 0.5 - window_height * 0.5))

    clear_surface.blit(no_move, no_move_rect)
    clear_surface.blit(turn_skipped, turn_skipped_rect)
    clear_surface.blit(close, close_rect)

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
            state.close_popup()

    screen.blit(clear_surface, (width / 4, height / 4))
    pg.display.flip()
