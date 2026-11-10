#import pandas as pd

#from OOP import fruits

#colors = ['red', 'green', 'blue', 'yellow',]
#for x in colors:
#   print(x)
#
# df = pd.read_csv('clean_final_data.csv')
# print(df)
# for product, row in df.iterrows():
#     print(f'product: {product}, Row:{row}')




# colors = ['red', 'green', 'blue', 'yellow']
# for x in colors:
#     print(x)
# Prints red green blue yellow
# Iterate through a string
# S = 'python'
# for x in S:
#     print(x)
# Prints p y t h o n

# Break in for Loop
# Break the loop at 'blue'
# colors = ['red', 'green', 'blue', 'yellow']
# for x in colors:
#     if x == 'blue':
#         break
#     print(x)
# Prints red green

# fruits = ['apple', 'banana', 'orange']
# for x in fruits:
#     if x == 'apple':
#         break
#     print(x)


#Range Function
# Generate a sequence of numbers from 0 6
# for x in range(7):
#     print(x)
# # Prints 0 1 2 3 4 5 6
# # You can generate a range of negative numbers as well.
# for x in range(-5,0):
#     print(x)
# # Prints -5 -4 -3 -2 -1
# """The range increments by 1 by default. But, you can specify a different increment by adding a step parameter."""
# # Increment the range with 2
# for x in range(2, 7, 2):
#     print(x)
# # Prints 2 4 6
#
# for x in range(4,5,-2):
#     print(x)
# for x in range(5,0,-2):
#     print(x)

#Class work
import random

Random_integer = random.randint(1, 10)
print(Random_integer)

# import random
#
# dice = random.randint(1, 6)
# print("You rolled:", dice)
#
# #Practical Ex: Random names
# import random
#
# names = ["Peter", "Waris", "King", "Elizabeth", "Lekan"]
#
# winner = random.choice(names)
#
# print("The winner is:", winner)


#While in Loop
# Iterate until x becomes 0
# x = 6
# while x:
#     print(x)
#     x -= 1

#Break in While Loop
#Exit when x becomes 3
# x = 6
# while x:
#     print(x)
#     x -= 1
#     if x == 3:
#         break


#Guess Game in Python
import random

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Generate a random number
secret_number = random.randint(1, 100)

# Initialize the guess
guess = 0

# Continue until the player guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Your guess is too high. Guess again.")
    elif guess < secret_number:
        print("Your guess is too low. Guess again.")
    else:
        print("Congratulations! You guessed the number correctly!")