def leap_year(year):
    if(year%4 == 0):
        if(year%100 == 0):
            if(year%400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

n = 2024
if leap_year(n):
    print(f"{n} is a leap year")
else:
    print(f"{n} is not leap year")