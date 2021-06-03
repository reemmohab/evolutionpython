# name = input("Type your name: ")
# name = "Reem"
# print(name + " Sleeping")


x = input("x: ")
y = input("y: ")
operation = input("select operation (+ - / *)")

if operation == "+":
    result = float(x) + int(y)

if operation == "-":
    result = float(x) - int(y)

if operation == "/":
    result = float(x) / int(y)

if operation == "*":
    result = float(x) * int(y)

print(result)

input("press Enter key to close")