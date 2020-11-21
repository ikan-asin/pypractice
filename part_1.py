tambah = lambda x,y : print('Hasil : ',x + y,'\n')
kurang = lambda x,y : print('Hasil : ',x - y,'\n')
kali = lambda x,y : print('Hasil : ',x * y,'\n')
bagi = lambda x,y : print('Hasil : ',x / y,'\n')

print('Kalkulator')
print('='*20)

while True:
	try :
		print('Kalo udah g mo pake klik Ctrl + c')
		x = int(input('Masukin angka pertama : '))
		y = int(input('Masukin angka kedua : '))
		print('+ / - / x / :')
		data = input('Yg mana : ')

		if data == '+':
			tambah(x,y)

		elif data == '-':
			kurang(x,y)

		elif data == 'x':
			kali(x,y)

		elif data == ':':
			bagi(x,y)

		else:
			print('Ummm...\n')

	except ValueError:
		print('Heii\n')
		continue

	except KeyboardInterrupt:
		print('\nByee')
		break