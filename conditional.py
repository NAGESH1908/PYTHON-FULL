light = input("light:")
if(light == "RED"):
    print("STOP")
elif(light == "GREEN"):
    print("GO")
elif(light == "YELLOW"):
    print("LOOK")
else:
    print("light is brocken")
    


    #ageee

age = int(input("age:"))
if(age>=18):
    print("can vot & applay for license")
else:
    print("cannot vot ")

#MARKS

#marks = int(input("marks:"))
marks = 85
if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks <90):
    grade = "B"
elif(marks >=70 and marks <80):
    grade = "c"
else:
    grade = "D"
print("grade of the student is:", grade)

#nesting
age = 34
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")  
else:
    print("cannot drive")