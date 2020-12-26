# some function
plus = lambda x,y : x + y
minus = lambda x,y : x - y
times = lambda x,y : x * y
divide = lambda x,y : x / y

print('Calculator')
print('='*20)

while True:
	try :
		print('If you have done, click Ctrl + c')
		x = int(input('First number : '))
		y = int(input('Second number : '))
		print('+ / - / x / :')
		data = input('Which one : ')

		if data == '+':
			a = plus(x,y)
			print('Answer : ',a,'\n')

		elif data == '-':
			b = minus(x,y)
			print('Answer : ',b,'\n')

		elif data == 'x':
			c = times(x,y)
			print('Answer : ',c,'\n')

		elif data == ':':
			d = divide(x,y)
			print('Answer : ',d,'\n')

		else:
			print('Ummm...\n')

	except ValueError:
		print('Heii\n')
		continue

	except ZeroDivisionError:
		print('U can\'t devide it with 0')

	except KeyboardInterrupt:
		print('\nByee')
		break