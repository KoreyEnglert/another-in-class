c = False;
while not c:
	year = input("Enter a year to check: ");
	try:
		year = int(year);
		c = True;
	except:
		print("That is not an integer!");

if year % 4 == 0:
	if year % 100 == 0 and year % 400 != 0:
		print(str(year) + ' is not a leap year.');
	else:
		print(str(year) + ' is a leap year.');
else:
	print(str(year) + ' is not a leap year.');
