import random
game = ['rock','paper','scissor']

while True:
	try:
		# randomize it
		game2 = random.choice(game)
		data = input('rock / paper / scissor : ')

		# here's the if-else magic happens
		if data == 'rock' and game2 == 'paper':
			print('U lose')

		elif data == 'rock' and game2 == 'scissor':
			print('U win')

		elif data == 'paper' and game2 == 'rock':
			print('U win')

		elif data == 'paper' and game2 == 'scissor':
			print('U lose')

		elif data == 'scissor' and game2 == 'rock':
			print('U lose')

		elif data == 'scissor' and game2 == 'paper':
			print('U win')

		else:
			print('Draw')

	except KeyboardInterrupt:
		print('\nByee')
		break