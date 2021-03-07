def leap(n):
    if n%400==0:
        return "Is a leap year"
    elif n%100==0:
        return "Is not a leap year"
    elif n%4==0:
        return "Is a leap year"
    else:
        return "Is not a leap year"

year = int(input("Please enter an integer to check whether that year is a leap year"))
print(leap(year))