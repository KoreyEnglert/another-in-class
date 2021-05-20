
def is_leap_year(a):
    year = 1;
    try:
        year = int(a);
    except:
        print("Invalid input");

    print(year);
    if year % 4 == 0:
    	if year % 100 == 0 and year % 400 != 0:
    		return False;
    	else:
    		return True;
    else:
    	return False;
