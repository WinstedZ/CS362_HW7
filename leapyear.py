def leap(n):
    if n%400==0:
        return "Is a leap year"
    elif n%100==0:
        return "Is not a leap year"