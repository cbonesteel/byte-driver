from enum import Enum

class MenuState(Enum):
    NONE = 0
    MAIN_MENU = 1
    TRACK_SELECT = 2
    MULTIPLAYER = 3
    END_GAME = 4