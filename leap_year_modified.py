
def is_leap_year(a):
    try:
    	year = int(year);
    except:
    	print("That is not an integer!");
        return False;

    if year % 4 == 0:
    	if year % 100 == 0 and year % 400 != 0:
    		return False;
    	else:
    		return True;
    else:
    	return False;
