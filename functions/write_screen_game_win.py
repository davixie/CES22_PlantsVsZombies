from constants import GAME_WIN
from menu_compra.buttons import Play_again
from menu_compra.buttons import Buttons

def write_screen_game_win(screen):
    screen.blit(GAME_WIN, (0, 0))
