# constants (will put in seperate file later)
SCREEN_WIDTH       = 160
SCREEN_HEIGHT      = 144
WINDOW_WIDTH       = SCREEN_WIDTH * 4
WINDOW_HEIGHT      = SCREEN_HEIGHT * 4

# game state
class gameState():
    LOGO     = 0
    TITLE    = 1
    GAME     = 2
    END      = 3
    curState = GAME
