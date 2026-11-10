#Mini calculator using function
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
   if num2 == 0:
       return "Error: Division by zero is not allowed."
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
    print("invalid operation")

#Lambda function
# add = lambda x, y: x + y
# result = add(5,10)
# print(f"Result: {result}")
#
# #default function
# def add(x, y):
#     return x + y
# result = add(5,10)
# print(f"Result: {result}")

#Map function
# def get_length(word):
#     return len(word)
#
# fruits = ("apple", "banana", "cherry")
# result = map(get_length, fruits)
# print(f"Result: {list(result)}")
#
# datascienceAvengers = ['victor', 'Ayo', 'Lekan', 'Waris', 'Elizabeth']
#
# avenger_lengths = list(map(get_length, datascienceAvengers))
# print(f'avenger_lengths: {avenger_lengths}')
#
# print(len('lekan'))
# print(len('Elizabeth'))


#Lambda + Map function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# multiples = lambda x: x * 2
# result = list(map(multiples, numbers))
# print(f"result: {result}")

def average_score(scores):
    return sum(scores) / len(scores)

students = {
    'John':[70, 80, 65],
    'Mary':[85, 90, 95],
    'David':[45, 55, 50],
    'Sarah':[90, 88, 92]
}
for name, scores in students.items():
    average = average_score(scores)
    result = list(map(average_score, students.values()))
    print(f'{name}: {average:2f}')