import sys
import pygame

def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.move_r()
			elif event.key == pygame.K_LEFT:
				ship.move_l()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				ship.move_over()
	
def update_screen(screen_set,screen,ship):
		screen.fill(screen_set.get_bg_color())
		ship.move()
		ship.blitme()
		pygame.display.flip()
		
