class cool:
	def __init__(self,*args):
		self.args = args

	def plus(self):
		a = 0
		for i in self.args:
			a = a + i
		print(a)

data = cool(2,10,-50,-60)
data.plus()