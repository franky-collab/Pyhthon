from datatype import greeting

text = "Hello World"
course = "SOFTWARE DEVELOPMENT"
greeting = "Hello there"
firstname = "Frank"
space = " "

print(text)
print(course)

#Accessing an element in a string
print(text[0])
print(text[2])

# Size of a string
print(len(text))

# Modifying a string
print(course.lower())
print(text.upper())

# String Concatenation - Joing strings
print(greeting + firstname)
print(greeting + " " +firstname)
print(greeting + space + firstname)
