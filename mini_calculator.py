print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Modulo (%)")
print("6. Exponent (**)")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (1 - 6): ")
num2 = float(input("Enter second number: "))
if operator == "1":
    print(round(num1 + num2))
elif operator == "2":
    print(round(num1 - num2))
elif operator == "3":
    print(round(num1 * num2))
elif operator == "4":
    print(round(num1 / num2))
elif operator == "5":
    print(round(num1 % num2))
elif operator == "6":
    print(round (num1 ** num2))
else:
    print("invalid operator")