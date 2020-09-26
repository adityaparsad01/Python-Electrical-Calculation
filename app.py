input1 = input('Enter L&T MTX MCCB Type: ')

MTX = input1.upper()

if MTX == "MTX1":
	current = float(input('MTX01 Triping Current: '))
	print('Total MTX01 Current is ' + str(current))
elif MTX == "MTX2":
	current = float(input('MTX02 Tripping Current: '))
	print('Total MTX01 Current is ' + str(current))
elif MTX == 'MTX3':
	current = float(input('MTX03 Tripping Current: '))
	print('Total MTX01 Current is ' + str(current))
else:
	print('Invalid MTX type. Try Ex:- mtx1,mtx2,mtx3') 