def is_leap(year):
    leap = True
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return leap
    else:
        leap = False
        return leap
