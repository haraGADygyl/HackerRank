import calendar

month, day, year = [int(x) for x in input().split()]

searched_day = calendar.weekday(year, month, day)

print(calendar.day_name[searched_day].upper())
