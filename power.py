def powTwoIter(number):
	isPowOfTwo=True;
	while (number != 1 and number > 0):
		if(number%2):
			isPowOfTwo = False
		number=number/2
	return isPowOfTwo and (number > 0)
