#WAP1
num = int(input("enter the num :"))
if(num %2 ==0):
    print("even")
else:
    print("odd")

#WAP2
a = int(input("enter the first num:"))
b = int(input("enter the secound num:"))
c = int(input("enter the third num:"))
if(a >=b and a >=c):
    print("a is the largest number:",a)
elif(b >= c):
    print("b is the largest number:",b)
else:
    print("c is the largest number:",c)

#WAP3

num = int(input("enter the number:"))
if(num%7 == 0):
    print("multiple by 7")
else:
    print("not multiple by 7")