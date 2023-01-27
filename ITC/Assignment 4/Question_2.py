def is_leap(year):
    if year >=1900 and year <= 10**5:
        if year % 400 == 0:
            leap = True 
        elif year % 4 == 0 or year % 100 !=0:
            leap = True
        else:
            leap = False 
    return leap

year = int(input())
print(is_leap(year))

