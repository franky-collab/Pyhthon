
number = 20 #Int
num = 34.67 #Float
greeting = "Hello there" #Str
ispythoninteresting = True #Boolean

# Data Structures
cars = ["Honda","porsche","Subaru"] #List
fruits = ("banana","apple","orange") # tuple
countries = { "Kenya","Tanzania","England","Italy"} #Set
details = {
    "Firstname" : "Harrison",
    "course" : "MIT",
    "nationality" : "Kenyan",
    "age" : 19
} # Dictionary - key-value pair






print(number)
print(num)
print(greeting)
print(ispythoninteresting)
print(cars)
print(fruits)
print(countries)
print(details)
print(details["nationality"])

# Determining the datatype
print(type(greeting))
print(type(countries))

# Typecasting - Converting one data type to another
print(float(number))
print(int(num))