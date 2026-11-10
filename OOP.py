class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
#
#     def display_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Department: {self.department}"
#
#
# student1 = Student("Victor", 21, "Computer Science")
# student2 = Student("Lekan", 22, "Computer Science")
#
# print(student1.display_info())
# print(student2.display_info())
# print(student1.age)
# print(student2.age)
#
# print(student1.department)
# print(student2.department)
#
# #Introducing Methods in Python
# class car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def introduce(self):
#         return f"This is a {self.make} {self.model} {self.year} car"
#
# car1 = car("Ford", "Mustang", "1999")
# car2 = car("Ford", "Mustang", "2000")
# print(car1.introduce())
# print(car2.introduce())

# class student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def introduce(self):
#         return f"My name is {self.name} and I scored {self.score}"
#
#
# student1 = student("Stan", 22, "70")
# student2 = student("David", 19, "84")
#
# print(student1.introduce())
# print(student2.introduce())
#
# #Encapsulation in Python
# class cat:
#     def __init__(self):
#         self.__sound = "Meow"
#
#     def speak(self):
#         print(self.__sound)
# speaking_cat = cat()
# speaking_cat.speak()
#
# class Animal:
#     def speak(self):
#         print("Animal makes sounds")
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# dog = Dog()
# dog.speak()
#
# cat = Cat()
# cat.speak()
#
# class student:
#     def __init__(self,name, score):
#         self.name = name
#         self.score = score
#
#     def average(self):
#         return sum(self.score)/len(self.score)
#
# class ScienceStudent(student):
#     pass
#
# class ArtStudent(student):
#     pass
#
# class CommercialStudent(student):
#     pass
#
# sciencestudent1 = ScienceStudent("Stanley", [81,90,78])
# ArtStudent1 = ArtStudent("Waris",[75,79,83])
# CommercialStudent1 = CommercialStudent("Elizabeth", [79,90,79])
#
# print(f"{sciencestudent1.name}'s average score is {sciencestudent1.average()}")
# print(f"{ArtStudent1.name}'s average score is {ArtStudent1.average()}")
# print(f"{CommercialStudent1.name}'s average score is {CommercialStudent1.average()}")
#
# class teacher:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def average(self):
#         return sum(self.salary)/len(self.salary)
#
# class scienceteacher(teacher):
#    pass
#
# class artteacher(teacher):
#     pass
#
# class commercialteacher(teacher):
#     pass
#
# scienceteacher1 = scienceteacher(" Mr Lanre", [15000, 23000, 30000,34000,40000,40000,43000,45000,45000,53000,55000,55000])
# artteacher1 = artteacher("Mrs Henry", [11000, 12000,15000,18000,18000,18000,23000,26000,28000,28999,33000,36000])
# commercialteacher1 = commercialteacher("Mr Sam",[17000,17000,18500,19000,19000,23000,23500,25000,25000,25000,30000.32000])
#
# print(f"{scienceteacher1.name}'s average salary for the year is {scienceteacher1.average()}")
# print(f"{artteacher1.name}'s average salary for the year is {artteacher1.average()}")
# print(f"{commercialteacher1.name}'s average salary for the year is {commercialteacher1.average()}")
#
# class fruits:
#     def fruit_type(self):
#         print("Mango", "Banana", "Apple")
#
# class vegetables:
#     def fruit_type(self):
#         print("Carrot", "Cabbage", "Spinach")
#
# class students:
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def introduce(self):
#         return f"My name is {self.name} and I scored {self.score}"
#     def get_grade(self):
#         if self.score >= 90:
#             return "A"
#         elif self.score >= 80:
#             return "B"
#         elif self.score >= 70:
#             return "C"
#         elif self.score >= 60:
#             return "D"
#         else:
#             return "F"
#
# John = students("John",26,98)
# Mary = students("Mary",26,88)
# David = students("David",26,88)
# studentname = input("Enter your name: ")
# if studentname == 'John':
#     print(John.introduce())
# elif studentname == 'Mary':
#     print(Mary.introduce())
# elif studentname == 'David':
#        print(David.introduce())
# else:
#     print('Student name not found')



class Account:
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount: float):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ₦{amount:,.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrawn: ₦{amount:,.2f}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.account_balance


# Create the first account
my_account = Account("1001", 100000.0, "Peter Alabi")

# Perform transactions
print(f"Account holder: {my_account.account_holder}")
print(f"Account number: {my_account.account_number}")

my_account.deposit(10000.0)
my_account.withdraw(5000.0)

print(f"Current balance: ₦{my_account.check_balance():,.2f}")

print("\n--- Second Account ---")

# Create another account
second_account = Account("1002", 25000.0, "Paul Adeyemi")
second_account.deposit(5000.0)
second_account.withdraw(40000.0)

print(f"Account holder: {second_account.account_holder}")
print(f"Current balance: ₦{second_account.check_balance():,.2f}")




class Account:
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount: float):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposit successful! New balance: ₦{self.account_balance:,.2f}")
        else:
            print("Enter an amount greater than zero.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Enter an amount greater than zero.")
        elif amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrawal successful! New balance: ₦{self.account_balance:,.2f}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account balance: ₦{self.account_balance:,.2f}")


# Create an account
account_holder = input("Enter your name: ")
account_number = input("Enter your account number: ")

my_account = Account(account_number, 0.0, account_holder)

print(f"\nWelcome, {my_account.account_holder}!")

# Banking menu
while True:
    print("\n===== BANKING MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: ₦"))
            my_account.deposit(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: ₦"))
            my_account.withdraw(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        my_account.check_balance()

    elif choice == "4":
        print(f"Thank you for banking with us, {my_account.account_holder}!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

