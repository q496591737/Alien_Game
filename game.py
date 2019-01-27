import pygame
import game_functions as gf
from ship import Ship
from settings import Settings


def run_game():
    
	pygame.init()
	screen_set = Settings()
	screen = pygame.display.set_mode((screen_set.get_width(),screen_set.get_height()))
	pygame.display.set_caption("Alien Invation")
	ship = Ship(screen)
	
	while True:	
		gf.check_events(ship)
		gf.update_screen(screen_set,screen,ship)
		
if __name__ == '__main__':
	run_game()
