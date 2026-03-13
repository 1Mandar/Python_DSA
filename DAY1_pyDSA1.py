#day-1 OF python dsa

# print your biodata like name age department 
# rollno mobno address

name=input ("enter your name:")
age=int(input("enter your age:"))
department=input("enter your department:")
rollno=int(input("enter your roll number:"))
mobno=int(input("enter your mobile number:"))
address=input("enter your address:")
print("name:",name)
print("age:",age)
print("department:",department)
print("roll number:",rollno)
print("mobile number:",mobno)
print("address:",address)


# Boolean (True / False)
# Example:
is_student = True
is_logged_in = False
print("Is the user a student?", is_student)
print("Is the user logged in?", is_logged_in)

# calculate Area of rectangle
length=float(input("Enter length"))
width=float(input("Enter width"))
# a=l*w
area=length*width
print("Area of rectangle = ",area)

name = "Mandar"
age = 19
height = 5.9
is_student = True


# Then check types:
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# calculate simple intrest
# SI=(p*R*t)/100

p=float(input("Enter principal:"))
r=float(input("enter rate:"))
t=float(input("Enter time"))
si=(p*r*t)/100
print("Simple intrest = ",si)
# swap two numbers
a=10
b=20
a,b=b,a
print("a = ",a)
print("b = ",b)
# find square,cube of a number
a=int(input("enter any number:"))
sqr=a*2
cube=a*3
# convert minits to hours
minits=int(input("Enter minits:"))
hours=minits/60
print("hours = ",hours)

# calculate Average of 3 number
print("Enter three numbers:")
num1=float(input())
num2=float(input())
num3=float(input())
average=(num1+num2+num3)/3
print("Average = ",average)

# convert celsius to fahrenheit
celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in fahrenheit = ",fahrenheit)

# convert km to meters
# meters=km*1000
km=float(input("Enter distance in kilometers:"))
meters=km*1000
print("Distance in meters = ",meters)

# convert rupees to dollar
rupees=float(input("Enter amount in rupees:"))
dollar=rupees/73
print("Amount in dollars = ",dollar)

# calculate total marks and percentage cgpa
print("Enter marks of 5 subjects:")
marks1=float(input())
marks2=float(input())
marks3=float(input())
marks4=float(input())
marks5=float(input())
total_marks=marks1+marks2+marks3+marks4+marks5
percentage=(total_marks/500)*100
cgpa=percentage/9.5
print("Total marks = ",total_marks)
print("Percentage = ",percentage)
print("CGPA = ",cgpa)

# Create variables for:
# name
# branch
# college
# year
name = "Amit"
branch = "Mechanical"
college = "RBU"
year = 3
print("Name = ",name)
print("Branch = ",branch)
print("College = ",college)
print("Year = ",year)

print("Hello Students")
age=21
#More examples
name = "Rahul"
salary = 50000
temperature = 36.5
print(type(name))
print(type(salary))
print(type(temperature))

price = 99.99
height = 5.8
temperature = 36.7
print(type(price))
print(type(height))
print(type(temperature))

#show types of variables

age = 21
print(type(age))

name = "Aakash"
print(type(name))
is_student = True
print(type(is_student))

#string
name = "Aakash"
city = "Pune"
course = "Python"
print("Name:", name)
print("City:", city)
print("Course:", course)

#typecasting
age="21"
age=int("21")
age=age+3
print(age)


age = "21"

# This is string, not number.
# Convert to integer:
age = int("21")

num = 10
# integer==>floating point number
# Convert to float:
num = float(10)

# Convert number to string
num = 100
print(type(num))
text = str(num)
print(type(text))

num1 = "10"
num2 = "20"
print(num1+num2)
result = int(num1) + int(num2)
print(result)

# taking input from user
age=input("enter your age:")
# ag1=int(input("Enter value ag1:")) type casting
print(age)
print(type(age))
# find your current age
byear=int(input("Enter your birth year:"))
cyear=2026
age1=cyear-byear
print(age1)

# Take input from user.
# Example:
age = input("Enter your age: ")
print(age)


# Explain:
# input() always returns string.
# Convert to integer:
age = int(input("Enter your age: "))

# Example:
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(age)

