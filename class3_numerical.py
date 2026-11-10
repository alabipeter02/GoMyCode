#1-Dimensional array
import numpy as np

one_dimensional_array = np.array([1, 2, 3, 4, 5])
#print(f"1-dimensional Array: {one_dimensional_array}")
# print(one_dimensional_array.shape)
#
# two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(two_dimensional_array.shape)
#
# a = np.array([1,2,0,1,0,2,0,2])
# print("Reshape_Array:", a.reshape(2,4))

# print(two_dimensional_array [1,2])

#Slicing an array
# an_array = np.array([6, 78, 9, 3, 42, 1, 3, 1])
# print(an_array.shape[:2])

# a = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(a[-1:])

#Reshaping in Python
# a = np.array([1,0,1,0,2,0,20])
# print('Reshape_Array:',(2,1))

#Random numbers in Python
# value1 = np.random.random((2,3))
# print('Random Value: ', value1)

# #Random whole numbers (integers) in Python
# value2 = np.random.randint(1, 20, size=(3,4))
# print('Random Integer:', value2)

#Random student scores
# score = np.random.randint(20, 100, size=(10))
# print('student Scores: ', score)
#
# #Creating an Array of Zeros
# zero_array = np.zeros((3,3))
# print('Zero Array:', zero_array)

#Creating an Array of ones
# one_array = np.ones(4)
# print('One Array:', one_array)

#Creating an array of a specific value
# specific_value = np.full((5,4), 8)
# print('Specific Value:', specific_value)

#The eye function in Python
# eye_array = np.eye(4)
# print('Eye Array:', eye_array)

#Numpy data type
# z = np.array(
#             [[1,2],[3,4]],
#             dtype=np.float64
# )
# print('Data type:', z)

#Numpy addition
# x = np.array(
#     [[1,2],
#      [3,4]
# ])
#
# y = np.array([
#     [5,6],
#     [7,8]
# ])
#
# print('Numpy Addition:', np.add(x,y))
#
#
# z = np.array(
#             [[1,2],[3,4]],
#             dtype=np.float64
# )
# print('Data type:', z)
#
# #Numpy addition
# x = np.array(
#     [[1,2],
#      [3,4]
# ])
#
# y = np.array([
#     [5,6],
#     [7,8]
# ])
#
# print('Numpy Addition:', np.add(x,y))
# print('Numpy Subtraction:', np.subtract(x,y))
# print('Numpy Multiplication:', np.multiply(x,y))
# print('Numpy Division:', np.divide(x,y))




class Independent:
    def __init__(self, name, country, state_of_origin, gender, age):
        self.name = name
        self.country = country
        self.state_of_origin = state_of_origin
        self.gender = gender
        self.age = age

    def introduce(self):
        if self.country != 'Nigeria':
            return f"Not from Nigeria: {self.name} is from {self.country}"

        if self.gender == 'Male':
            title = 'Mr'
        elif self.gender == 'Female':
            title = 'Mrs'
        else:
            title = ''

        nigeria_age = 2026 - 1960

        return (f"Hello {title} {self.name} from "
                f"{self.state_of_origin}, Nigeria. "
                f"Happy Independent day {nigeria_age} "
                f"years of Independence!")

# Allow user to enter details
name = input("Enter your name: ")
country = input("Enter your country: ")
state_of_origin = input("Enter your state of origin: ")
gender = input("Enter your gender: ")
age = input("Enter your age: ")





# person1 = Independent('Peter', 'Nigeria', 'Kogi', 'Male', 19)
# person2 = Independent('Waris', 'Nigeria', 'Ogun', 'Male', 25)
# person3 = Independent('King', 'America', 'Texas', 'Male', 25)
# person4 = Independent('Elizabeth', 'Nigeria', 'Osun', 'Female', 25)
person5 = Independent('Lekan', 'Nigeria', 'Lagos', 'Male', 22)



print(person5.introduce())






