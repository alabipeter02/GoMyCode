#Creating Functions in Python
# def square(number):
#     return number * number
#
# result = square(49)
# print(result)

#Greet function
# def greet(name):
#     return f'Hello, {name}, Wishing you a great day ahead!'
#
# #greeting = greet("Alice")
# greeting = greet (input("Enter your name: "))
# print(greeting)

#Creating a sum function
# def add_numbers(num1,num2):
#     total= num1 + num2
#     return total
#Example suage:
# sum_result = add_numbers(240, 119)
# print(sum_result)
#
# #Creating a function with multiple parameters
# def operations(num1,num2,num3):
#     peter = (num1 + num2) / num3
#     return peter
# Calculation = operations(20, 30, -5)
# print(Calculation)

#Creating a function default argument
# def add_number(num1,num2):

#Mini calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
   if num2 == 0:
       return "Error: Division by zero is not allowd."
   return num1 / num2
firstnumber = float(input("Enter first number: "))
secondnumber = float(input("Enter second number: "))
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter your Choice (1/2/3/4): ")

if operation == "1":
   result = add(firstnumber, secondnumber)
   print(f"Result: {result}")
elif operation == "2":
   result = subtract(firstnumber, secondnumber)
print(f"Result: {result}")
elif operation == "3":
  result = multiply(firstnumber, secondnumber)
print(f"Result: {result}")
elif operation == "4":
result = divide(firstnumber, secondnumber)
print(f"Result: {result}")
else:
    print("invalid operation selected")

