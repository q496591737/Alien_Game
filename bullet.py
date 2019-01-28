import pygame


class Bullet():
	def __init__(self,screen,ship):
		self.__screen = screen
		self.__ship = ship
		self.__image = pygame.image.load('images/bullet.png')
		self.__rect = self.__image.get_rect()
		self.__ship_rect = self.__ship.get_rect()
		self.__rect.centerx = self.__ship_rect.centerx
		self.__rect.bottom = self.__ship_rect.top
		self.__bottom = float(self.__rect.bottom)
		self.__speed = 0.2
		#self.__screen_rect = self.__screen.get_rect()
		#self.__rect.centerx = self.__screen_rect.centerx
		#self.__rect.bottom = self.__screen_rect.bottom
	def blitme(self):
		self.__screen.blit(self.__image,self.__rect)
		self.__bottom -= self.__speed
		self.__rect.bottom = int(self.__bottom)
		
		
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	bullet = Bullet(screen)
	while True:
		bullet.blitme()
		pygame.display.flip()
