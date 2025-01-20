# for i in [1, 2, 3, 4]:
#     print(i)

# word = "hello"
# for char in word:
#     print(char)

# n = 21
# for i in range (n+1):
#     print(i**2)

# for i in range (1,10,4):  
#     print(i)    

# i = 1
# while i <= 20:
#     if i %2==0:
#         print (i)
# i = i + 1 

# Develop a program that calculates the area of a triangle given its base and height.

# b= int(input("enter b :")) 
# h=int(input("enter h :")) 
# area = (b*h)/2  
# print("Area of Triangle is : ") 
# print(area)

import numpy as np

# # Create a 3x4 array filled with zeros
# arr = np.zeros((3, 4))

# # Print the array and its shape
# print(arr)
# print("Shape of the array:", arr.shape)

# You have a 1D NumPy array with 12 elements. Write a code to reshape it into a 2D array with shape (3, 4) and print the reshaped array.

# arr = np.arange(12)
# reshaped_arr = arr.reshape(3, 4)
# print(reshaped_arr)

# How can you create a NumPy array of shape (2, 5) that is filled with the number 7?

# arr = np.full((2,5),7)
# print(arr)

# Create a NumPy array of shape (2, 3, 4) filled with random integers. Print the shape and size attributes.

# arr = np.random.randint(1, 10, size=(2, 3, 4))

# print(arr)
# print("Shape of the array:", arr.shape)
# print("Size of the array:", arr.size)

# nested if

# number = int(input("Enter a number: "))

# if number > 0:
#     if number %2==0:
#         print("this is even number")
#     else:
#         print("this is odd number")    
# else:
#     if number ==0:
#         print("this is zero")
#     else:
#         print("this is negative number")           

# Value = None
# if Value :
#     print("Value is true")
# else:
#     print("value is false")      
       
# predefined username and password
# predefined_username = 'Madhav'
# predefined_password = 'Pass101'

# prompts the user to enter a username and password 
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# # # username and password match 
# if username == predefined_username:
#     if password == predefined_password:
#         print("Welcome! Login was successful.")
#     else:
#         print("Incorrect Password!")
# else:
#     print("Invalid Username!")

# python program to create a simple calculator

# def add (num1,num2):
#     return num1 + num2
# def subs (num1,num2):
#     return num1 - num2
# def multiply (num1,num2):
#     return num1 *  num2
# def divide (num1,num2):
#     return num1 / num2
# def avg(num1,num2):
#      return (num1 + num2)/2 

# print("Please select a operation:\n " \
#       "1. Addition\n" \
#       "2. Substraction\n" \
#       "3. Multiplication\n" \
#       "4. Division\n" \
#       "5. Average\n") 

# select = int(input("Select a operation from 1,2,3,4,5: ")) 

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if select == 1:
#     print(number1, "+", number2, "= ",add(number1, number2))

# elif select == 2:
#      print(number1, "-", number2, "= ", \
#            sub(number1, number2)) 
     
# elif select == 3:
#      print(number1, "*", number2, "= ", \
#            multiply(number1, number2))
     
# elif select == 4:
#      print(number1, "/", number2, "= ", \
#            divide(number1, number2))

# elif select == 5:
#      print("(",number1, "+", number2, ")", "/", "2", "= ", \
#            avg(number1, number2))
     
         
# else:
#      print("Invalid operation! Pls select again!")

# even_num = [ i for i in range(1,10) if i%2==0 ]
# print(even_num)

# str = input("enter a string :")
# if str == str [::-1]:
#     print("string is a palindrom")
# else:
#     print("string is not palindrom")    

# python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# for i in range(0,5):
#  print(python_students[i])

# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)  # The list will be shuffled

# import random
# print(random.choice([1, 2, 3, 4, 5]))  # It will randomly print 1, 2, 3, 4, or 5

# import random
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.sample(my_list, 5))  # Randomly selects 3 unique elements

# import random
# # random_float = random.random()  # Generates a random float between 0 and 1
# # print(random_float)

# random_int = random.randint(1,100) 
# print(random_int)

# import random
# random_float = random.uniform(5, 10)  # Generates a random float between 5 and 10
# print(random_float)

# import random
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sample = random.sample(my_list, 3)  # Selects 3 random elements without replacement
# print(sample)

# star pattern

# n=10
# for i in range (1,n+1):
#     for j in range(1, i+1):
#         print(j,end="")
#     print()    

    # Solution to print the pyramid number pattern
n = 5
for i in range(1, n + 1):
    # Print spaces for the pyramid shape
    for j in range(n - i):
        print(" ", end="")
    
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()


