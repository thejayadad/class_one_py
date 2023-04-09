

# # PYTHON BEGINNER CLASS

# #CAPTURING MY NOTES WHILE IN THE LECTURE

# #DEFINIG VARIABLE
# x = 9
# first_name = "jace"
# last_name = "goat"
# print(x)
# print(first_name, last_name)
# print(type(first_name))
# print(type(100))
# print(type(1.99))


# print(type(2j))  #COMPLEX TYPE

# print("1" + "1")

# # BOOLEAN STARTS WITH CAP
# true = True
# print(true)

# #<---------- DATA STRUCTURES TYPES----------------->
# #LIST

# my_list = [1,22,66,88]
# print(my_list)
# print(type(my_list))
# list_of_strings = [[123,],  [4, 5,6]]
# print(list_of_strings)


# #SETS - THESE PRINT THE  {} BRACKETS
# my_set = {1,2,3,4}
# print(my_set)

# #LEN GIVE COUNT
# print(len(my_list))

# # my_tuple.append(3)#THIS WILL GIVE AN ERROR

# # TUPLES ARE DECLARED WITH PARATHENSIS
# my_tuple = (1,2,3)
# print(my_tuple)

# # CANT APPEND OR ADD TO THESE

# my_list.append(8)
# print(my_list)
# #
# #DICTIONARY - DEFINED WITH CURLY BRACKETS PROVIDE KEY AND VALUE PAIRS
# my_dictionary ={
#     'potato': 'fries  ',
#     'apple': 'apple pie'
# }

# print(my_dictionary)

#<--------ARITHMETIC OPERATORS------->

#MODULAR WORKS JUST AS DOES IN OTHER LANGUAGE
#STRINGS ARE ADDED TOGEHTER OR COMBINED

#COMPARISON LOGICAL AND MEMBERSHIP WORK SAME AS OTHER PL

#MEMBERSHIP OPS REPRESENT IF PRESENT - STRINGS AS WELL

#<----CONTROL FLOW--->>

#IF/ELSE

# x = False
# if x:
#     print("simple if statement")
# else:
#     print("False")

# a= 1
# b = 2
# c = 3

# if a > b:
#     print("A wins")
# else:
#     print("B wins")


#LOOPS
# a = [1,2,3,4,5]
# for it in a:
#     print(it)

#WHILE LOOP

# a = 0
# while a< 5:

#     print(a)
#     a += 1

#<---------------------FUNCTIONS----------------------------->

# def mutl_by_three(val):
#     return 3 * val


# print(mutl_by_three(9))

# a = [1,3,76,88]
# def append_list(a):
#     a.append()

# print(mutl_by_three())

#<---------------OBJECTS AND CLASSES ------------------------------->
#CLASS

# class Dog:
#     def __init__(self,name): #<---ATTRIBUTES
#         self.name = name
#         self.tail = "yes"

#     def speak(self):
#         print(self.name + ' says: Bark!') #<------ METHOD


# my_dog = Dog("Spike")
# her_dog = Dog("jill")

# my_dog.speak()
# her_dog.speak() #<---CALLING THE FUNCTION



# #FACTORIAL FUNCTION
# def factorial(num):
#     if type(num) is not int:
#         return None
#     if num < 0:
#         return None
#     if num == 0:
#         return 1

#     i = 0
#     f = 1
#     while i < num:
#         i = i + 1
#         f = f + i

#     return f

# #FACTORIAL FUNCTION DOING RECURSION
# def factorial_recursion(num):
#     if type(num) is not int:
#         return None
#     if num < 0:
#         return None
#     if num == 0:
#         return 1

#     return num * factorial(num -1)


#<------------INTS & FLOATS ---------------->

# x = 20/4
# print(x)

# print(4 + 7.0)
# print(4 * 5.9)
# print(int(4 * 5.9))
# print(14/6)
# print(round(14/6))

# print(1.2 - 1.0)



# #INT CLASS
# print("100")
# print(int("100"))
# print(type("100"))


#<------BOOLEANS------>
#CASTING BOOLEANS
#BOOLEAN IS BOOLEAN
# print(bool(1))

# print(bool("True"))
# print(bool("False"))
# print(bool({})) #<---WILL PASS FALSE
# a = 2
# b= 2
# print (a == b)

# weather_is_nice = False
# have_umbrella = True
# if(not have_umbrella or weather_is_nice):
#     print("stay inside")
# else:
#     print("go for a swim")



#<------STRINGS------------->
#Slicing
# name = "jason"
# print(name[0])
# print(name[0:2])

# #Get ':' short hand no need for the zero
# #to get to end of the string num:

# print(name[2:]) #<-- end of string

# #works same with last

# my_list = [1,2,3,4,5]
# print(my_list[1:3])

# #TO FORMAT USE 'f' - string
# print(f"my name is "  + name)

# #MULTI LINE STRING
# my_string = """
# just add the extra quote
# another line
# """

# print(my_string)


# #<------BYTES----->
# print(bytes(3)) #<--- 8 bites to byte b in front is bytes object


#<-Converting hexadecimal to decimal number

# hex_numbers = {
#     '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
# }

# def hex_to_dec(hexNum):
#     for char in hexNum:
#         if char not in hex_numbers:
#             return None
#         if len(hexNum) == 3:
#             return hex_numbers[hexNum[0]] * 256 +  hex_numbers[hexNum[1]] * 16 + hex_numbers[hexNum[2]]

#         if len (hexNum) == 2:
#             return hex_numbers[hexNum[0]] * 16 + hex_numbers[hexNum[1]]
#         if len (hexNum) == 1:
#             return hex_numbers[hexNum[0]]


# print(hex_to_dec('A'))
# print(hex_to_dec('B'))
# print(hex_to_dec('C'))
# print(hex_to_dec('a'))


#<-----BRB Break at 2:45 - 3p

# #<---LIST------------------>
# my_list = [1,2,3,4,5,67,8]
# my_list[4]
# print(my_list)
# print(my_list[::3])
# for i in range (10):
#     print(i)

# my_list_two = my_list
# my_list_two.append(2)
# print(my_list_two)
# my_list_two.pop() #<----REMOVE LAST ITEM
# print(my_list_two)

# #SEPERATE COPY STORIED IN LIST
# a = [1,3,4,5,6]
# b = a.copy()
# a.append(10)
# b.append(30)
# print(a)
# print(b)

# #<---------------------TUPLES AND SET---------------->

# #SET
# a = {'e', 'y', 'i'}
# print(a)

# #REMOVE DUPLICATES
# my_list = ['a', 'b', 'a', 'b', 'g', 'p', 'o', 'p', 'p']
# my_list = list(set(my_list))#<---REMOVES THE DUPLICATES
# print(my_list)


# #SETS ARE RANDOMIZE

# number = 1
# number = number * 2
# print(number)


# my_list = list(set(my_list))
# print(my_list)

# #RETURN MULTIPLE VALUES
# def multi():
#     return 1,3,4,5,6


# # print(multi())

# #<------DICTIONARY----->

# animals = {
#     'a': 'dogs',
#     'b': 'cat',
#     'c': 'fish'
# }

# print(animals['a'])
# animals['c'] = 'bear'
# print(animals['c'])


# #conver to list

# print(list(animals.keys()))


#<----------------LIST COMPREHENSIONS-------------------->
# my_list = [1,2,3,5,6,]

# [2*item for item in my_list]
# print(my_list)

# my_list = list(range(100))
# filtered_list = [item for item in my_list if item % 10 == 0]

# print(filtered_list)

# my_string = 'my name is jace. i live in tennessee'
# my_string.split('.') #<---- splits at the charact inside of split
# print(my_string.split('.'))

# print(my_string.replace('jace', 'jada'))#<---replacing word


# #NESTED LIST
# # [[clean_word(word) for word in sentence.split()] for sentence in my_string]

# animal_list = [('a', 'adam'), ('b' 'brian'), ('c' 'charles')]
# # animals = {item[0]: item[1] for item in animal_list}
# # print(animals)


# #<----CONTROL FLOW----------------->

# for n in range(1, 101):
#     if n % 15 ==0:
#         print("Fizz buzz")
#     else:
#         if n % 3 == 0:
#             print("Fizz")
#         else:
#             if n % 5 == 0:
#                 print("buzz")
#             else:
#                 print(n)



# n = 3
# print("Fizz" if n % 3 == 0 else n)


# #WHILE LOOP
# from datetime import datetime

# # print(datetime.now())


# wait_until = datetime.now().second * 3
# print(wait_until)

# while True:
#     if datetime.now().second == wait_until:
#         print(f"we are at {wait_until} seconds")
#     break

#Continue skips lines that follows inside while loop

#FOR LOOP

# my_list =[1,2,3,4,5,6]
# for item in my_list:
#     print(my_list)
#     print(item)



#PRIME # BETWEEN 2 and 100

# for number in range(2, 100):
#     for factor in range(2, int(number ** 0.5) + 1):
#         if number % factor == 0:
#             break

#     else:
#         print(f"{number} is prime")


# #CREATE FUNCTION ALL PRIMES UP TO
# def all_primes_upto(num):
#     primes = [2]
#     for number in range(3, num):
#         sqrtNum = number**.5
#         for factor in primes:
#             if number % factor == 0:
#                 break #<---NOT PRIME
#             if factor > sqrtNum:
#                 primes.append(number)
#                 break
#     return primes

# print(all_primes_upto(40))

#<-------------------FUNCTION-------------------->

# def perform_operation(num1, num2, operation):
#     if operation == "sum":
#         return num1 + num2
#     if operation == "multiply":
#         return num1 * num2
#     if operation == "divide":
#         return num1 / num2

# print(perform_operation(4, 5, "multiply"))

# print(perform_operation(4, 5, "sum"))

# print(perform_operation(4, 5, "divide"))


# def per_ops(*args): #<-- ref to whats being passed in
#     print(args)


# per_ops(8,9,4)

# def perf_oper(*args, operation ="sum"):
#     if operation =="sum":
#         return sum(args)
#     if operation =="multiply":
#         return math.prod(args)


# print(perf_oper(10,3,4, operation="sum"))

#<-----------------------VARIABLES & SCOPES--------------->

# def perform_ops(num1, num2, operation="sum"):
#     print(locals())


# perform_ops(1,3, operation="mulitply")


# #GLOBALES
# print(globals())#<---- behind the scenes



# def function (varA, varB):
#     print(locals())

# def function2(varC, varB):
#     print(locals())


# function(1,3)
# function2(3, 4)

#<-----------------------15 min break bb 4:45------------------------>

#CLASSES & OBJECTS

# class Dog:
#     def __init__(self, name):
#         self.name = name
#         _legs= 4


#     def get_legs(self):
#         return self._legs


#     def speak(self):
#         print(self.name + " is barking - ROOF!!! ROOF!!")


# my_dog = Dog("Spike")
# print(my_dog.name)
# print(my_dog.get_legs())

#<---static and instance methods----------------->


# x = input("name")
# print(x)

import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Movies
               (Title TEXT, Director TEXT, Year INT)''')

# #INSERT RECORD INTO DATABASE
# cursor.execute("INSERT INTO Movies VALUES('Taxi Driver', 'Martin Lawrence', 2002)")

#RETRIEVE DATA
cursor.execute("SELECT * FROM Movies")
print(cursor.fetchone())

#INSERT SEVERAL ITEMS TO DATABASE
famousFilms = [('Friday', 'Chris Tucker', 1996),
               ('Home Alone', 'Mcconneclly Colugin', 1992),
               ('God Father', 'Al Pachino', 1971)]

#INSERT MORE THAN ONE ITEM INTO DATABASE
cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)
#SAVE INTO A VARIABLE
records = cursor.execute("SELECT * FROM Movies")
#FETCH ALL ITEMS
print(cursor.fetchall())

#TO SAVE CHANGE _ COMMIT
connection.commit()

#TO CLOSE THE CONNECTION
connection.close()
