year = input("Enter a year to check: ");

if int(year) % 4 == 0:
	if int(year) % 100 == 0 and int(year) % 400 != 0:
		print(year + ' is not a leap year.');
	else:
		print(year + ' is a leap year.');
else:
	print(year + ' is not a leap year.');
