# Built-n Functions

y = max(56,75,35,57)
print("The maximum value is",y)

x = min(4,45,64,75,42,23)
print("The minimum value is",x)

# User-defined functions
def name():
    print("Frank")
name() # Calling a function

def product():
    a = 10
    b = 20
    print(a * b)
product()

# Parameter/variable and Arguement/value
def sum(num1,num2):
    print(num1 + num2)
sum(5,6)
sum(10,37)

def Employee(name,age,position,salary):
    print(name,age,position,salary)

Employee("Frank",78,"CEO",43789900)
Employee("Eden",38,"Secretary",43000)
Employee("Gorge",40,"Director",437300)
Employee("Mary",58,"Clerk",59000)

# A program to display details of students
# Fullname,age,course,gender,nationality

def Student(Fullname,age,course,gender,nationality):
    print(Fullname,age,course,gender,nationality)
Student("Frank",67,"MIT","Male","Kenyan")
Student("George",37,"Cybersecurity","Male","American")
Student("Justin",40,"Data science","Male","Kenyan")
Student("Loice",28,"Software development","female","Mexican")
Student("Tim",64,"MIT","Male","German")


