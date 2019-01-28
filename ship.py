import pygame
from bullet import Bullet

class Ship():
	def __init__(self,screen):
		self.__screen = screen
		self.__image = pygame.image.load('images/ship.png')
		self.__rect = self.__image.get_rect()
		self.__screen_rect = screen.get_rect()
		self.__rect.centerx = self.__screen_rect.centerx
		self.__rect.bottom = self.__screen_rect.bottom
		self.__move = 0
		self.__speed = 0.1
		self.__center = float(self.__rect.centerx)
		self.__bullets = []
		
	def blitme(self):
		self.__screen.blit(self.__image,self.__rect)
		for bullet in self.__bullets:
			bullet.blitme()
	def move_r(self): 
		self.__move = 1
	
	def move_l(self):
		self.__move = -1
	
	def move_over(self):
		self.__move = 0
	
	def move(self):
		if self.__move == 1 and self.__rect.right < self.__screen_rect.right:
			self.__center += self.__speed
		elif self.__move == -1 and self.__rect.left > 0:
			self.__center -= self.__speed
		self.__rect.centerx = self.__center
	
	def fire(self):
		bullet = Bullet(self.__screen,self)
		self.__bullets.append(bullet)
		
	def get_rect(self):
		return self.__rect
