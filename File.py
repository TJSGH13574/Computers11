#part 1
#Asks the user for an age
"""
Evaluates the person's identity by identifying whether their age is above 18(adult), 
below 18 and above 13 (teenager) or below 13 (child)
"""
print("please give me an age",end = "\n")
age = int(input())
if age >= 18:
    print("you are an adult",end = "\n")
elif 13 <= age < 18:
    print("you are a teenager",end = "\n")
else:
    print("you are a child",end = "\n")

#part 2
#Ask the user for a number
print("now give me a number",end = "\n")
num = int(input())
#Compares and identifies if the number is greater, equal, or less than 0
if num > 0:
    print("The number is positive",end = "\n")
elif num == 0:
    print("The number is zero",end = "\n")
else:
    print("The number is negative",end = "\n")

#part 3
#Ask the user for a student's grade for an exam
#Check if the student's score is above 90, 80, 70, or 60 to determin their grade
print("now give me a score of a student on an exam ",end = "\n")
grade = int(input())
if grade >= 90:
    print("The student got an A",end = "\n")
elif 80 <= grade < 90:
    print("The student got a B",end = "\n")
elif 70 <= grade < 80:
    print("The student got a C",end = "\n")
elif 60 <= grade < 70:
    print("The student got a D",end = "\n")
else: 
    print("The student got an F ",end = "\n")

#part 4
#Ask the user for a temperature
#Identify if the temperature is cold, warm, or hot
print("Now give me a temperature in celsius ",end = "\n")
temperature = int(input())
if temperature >= 25:
    print("Its hot outside",end = "\n")
elif 10 <= temperature < 25:
    print("Its warm out there",end = "\n")
else:
    print("Its cold out there",end = "\n")