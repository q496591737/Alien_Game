class Settings():
	def __init__(self):
		self.__screen_width = 600
		self.__screen_height = 400
		self.__bg_color = (255,255,255)
	
	def get_width(self):
		return self.__screen_width
	
	def get_height(self):
		return self.__screen_height
		
	def get_bg_color(self):
		return self.__bg_color
