
#List in Python
# fruits = ['apple', 'banana', 'cherry']

# print('original list:', fruits)
#
# fruits.append('orange')
# print('updated list:', fruits)
#
# fruits.insert(2, 'grape')
# print('latest updated list:', fruits)

#Joining two list
# numbers = [1, 2, 3, 4, 5, 6]
# print('numbers list:', numbers)

# even_numbers = [2, 4, 6, 8]
# print('even numbers:' , even_numbers)
#
# numbers.extend(even_numbers)
# print('updated numbers list:', numbers)

#Deleting in Lists
# del numbers[4]
# print('updated numbers list:', numbers)
# print(numbers)

#Class Activity
# list = [17, 38, 10, 25, 72]
# list.sort()
# print('sorted list:', list)
#
# list.append(12)
# print('updated list:', list)
#
# list.reverse()
# print('reversed list:', list)
#
# index = list.index(17)
# print('index:', index)
#
# list.remove(38)
# print('remove 38:', list)

#Dictionary
student = {
    'name': 'victor',
    'age': 20,
    'deparment': 'data science',
    'course': ['python', 'Data Analysis'],
    'reg_number': 2020,
}
print('student information:', student)
print('student name:', student['name'])

student['GPA'] = '4.8'
print('updated student GPA:', student['GPA'])
print('student information:', student)

student.clear()
print('student information:', student)

#Updating my Dictionary
student['GPA'] = '2.5'
print('updated student GPA:', student['GPA'])
print('student information:', student)

#Dictionary Class work
student = {
    'name': 'Peter',
    'age': 21,
    'major': 'Master',
    'deparment': 'data science',
}
print('student dictionary:', student)
print('student information:', student)

student_keys = student.keys()
print('student_values):', student_keys)

student['age'] = '22'
print('student updated age',student)

student['graduation_year'] = 2025
print('student updated graduation_year',student)

student['grade'] = 'first_class'
print('student updated grade',student)


#set in python
# mySet = {101, 102, 103, 104, 105}
# print('My_set:',mySet)
#
# mixed_set = {1, 2,3, 'Ayo', 'Victor', 10.25,20.50, 2, 3, 3, 2}
# print('Mixed_Set:', mixed_set)

# mixed_set.add('Lekan')
# print('Mixed_Set:', mixed_set)
#
# myset.update(fruits)
#
# setsum = sum(mySet)
# print('SetSum:', setsum)
#
# #Tuples in Python
# myTuple = (1, 2, 3, 4)
# print('MyTuple:', myTuple)

# Original tuple
my_tuple = (1, 2, 3)

# Element to add
element = 4

# Convert tuple to list
my_list = list(my_tuple)

# Add the element
my_list.append(element)

# Convert back to tuple
my_tuple = tuple(my_list)

print(my_tuple)
