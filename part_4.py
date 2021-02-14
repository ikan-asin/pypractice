import random

class game:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.level = 1

	def info(self):
		print('name :', self.name)
		print('exp :',self.exp)
		print('level :',self.level,'\n')

	def attack(self):
		self.exps = random.randint(20,30)
	
	def collect_exp(self):
		game.attack(self)
		
		self.exp += self.exps
		if self.exp > 200:
			print(self.name, 'level up !')
			self.level += 1
			self.exp -= 200

data = game('ikan')

for i in range(10):
	data.collect_exp()
	data.info()