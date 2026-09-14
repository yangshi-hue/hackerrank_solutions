def dayOfProgrammer(year):
    #transition year
    if year == 1918:
        return "26.09.1918"
    #julian calender
    if year < 1918:
        leap = year % 4 ==0
    else:
        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    if leap:
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)