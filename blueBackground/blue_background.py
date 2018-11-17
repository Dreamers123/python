import game_function as gf
from settings import Settings
from character import Character
import  pygame
def run_game():
 pygame.init()

ai_settings = Settings()
screen = pygame.display.set_mode( (ai_settings.width, ai_settings.height))
pygame.display.set_caption("Blue Background")
character = Character(screen)
while True:
   gf.check_events()
   gf.update_screen(ai_settings, screen, character)


run_game()