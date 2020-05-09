year = int(input("Enter the year"))

if year%100==0:
    if year%400==0:
        print("This is Leap year")
    else :
        print("This is not a leap year")
else :
    if year%4 == 0:
        print("This is a leap year")
    else :
        print("This is not a leap year")


