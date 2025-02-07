# Prompt the user input

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Operation

sum = ("sum: {} + {} = {}".format(a,b,a+b))
diff = ("Difference: {} - {} = {}".format(a,b,a-b))
product = ("Product: {} * {} = {}".format(a,b,a*b))
quotient = ("Quotient: {} / {} = {}".format(a,b,a/b))

# End results

print("The sum:",sum)
print("The difference:",diff)
print("The product:",product)
print("The quotient:",quotient)

