from calendar import isleap


def is_year_leap(year):
    if isleap(year):
        print("True")
    else:
        print("False")


x = is_year_leap(2020)
