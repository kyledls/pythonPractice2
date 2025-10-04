def is_leap_year(year):
    leap_year_status = False
    if year % 4 == 0:
        leap_year_status = True
    else:
        leap_year_status = False

print(is_leap_year(2025))
