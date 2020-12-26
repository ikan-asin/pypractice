print('Welcome !\n')

# make some square
for i in range(5):
	for a in range(5):
		print('+',end='')
	print('')

print('')

# make a rectangle
for i in range(0,3):
	for x in range(0,8):
		print('+',end='')
	print('')

print('')

# make a half diamond
for a in range(1,6):
	for v in range(1,a+1):
		print('+',end='')
	print('')

for r in range(1,6+1):
	for a in range(r,6+1):
		print('+',end='')
	print('')

# make a nice diamond
for k in range(1,5+1):
	print(' '*(6-k)+'+ '*k)

for a in range(6,0,-1):
	print(' '*(6-a)+'+ '*a)