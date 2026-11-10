import numpy as np
import json
#Read mode in files handling

with open('Waris.txt', 'r') as file:
    content = file.read()
    #print(content)

#To read multiple lines in a file
# with open('Waris.txt', 'r') as file:
#      for line in file:
#     #print(line.strip())

#To write to a file in files handling
with open('Ayo.txt', 'w') as file:
    file.write("Hello, My name is Ayo.\n")
    file.write("I am a Data science student in GoMyCode.\n")
    file.write("I am interested in machine learning and artificial intelligence.\n")
    #print("file written successfully.")

#Append mode in files handling
with open('waris.txt', 'a') as file:
    file.write("\nWaris is a lazy student, but he is a good learner.")
    #print(f'file appended successfully.')

with open('waris.txt', 'r') as file:
    content = file.read()
    #print(content)

#Using Numpy genfromtxt() to read data from a text file
data = np.genfromtxt('student_performance_activity.csv', delimiter=',', dtype=None, names=True)
#print(data)

#writing JSON Data to a file
data = {
    "name": "Waris",
    "age": 25,
    "City": "Ilorin-west",
    "Country": "Nigeria"
}
with open('data.json', 'w') as file:
    json.dump(data, file)

#Reading JSON Data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)