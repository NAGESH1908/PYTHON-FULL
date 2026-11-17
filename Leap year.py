year = int(input("ENTER YEAR: "))

Leap = False

if year%4 == 0:
    Leap = True
elif year%100 == 0 and year%400 != 0:
    Leap = False
else:
    Leap = False
print(Leap)