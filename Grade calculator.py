m= int(input("marks in maths: "))
s= int(input("marks in science: "))
e= int(input("marks in english: "))

Total_marks = m+s+e
Average = Total_marks/3
Percentage = (Total_marks/300)*100
if Percentage >90:
    Grade ="A"
elif Percentage>80 and Percentage<=90:
    Grade = "B"
elif Percentage>70 and Percentage<=80:
    Grade = "C"
else:
    Grade = "F"

print(f"TOTAL MARKS : {Total_marks} \n AVARAGE: {Average} \n PERCENTAGE : {Percentage} \n GRADE : {Grade}")
