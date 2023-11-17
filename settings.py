# game settings 
WIDTH = 480
HEIGHT = 480
FPS = 30
SCORE = 0

# player settings
PLAYER_JUMP = 20
PLAYER_GRAV = 1.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (150, 200, 255)

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, " "),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, " "),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (350, 200, 100, 20, " "),
                 (175, 100, 50, 20, " "),
                 (45, 250, 50, 20, " "),
                 (280, 350, 50, 20, " ")
                 ]



# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 1000
HEIGHT = 900
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GROUND = (0, HEIGHT - 40, WIDTH, 40, "normal")
PLATFORM_LIST = [
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "normal")]