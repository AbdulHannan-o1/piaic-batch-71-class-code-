
# single and multi line comments
# hash (#) is use for single line comments
# triple quotes (''' or """) are used for multi line comments
# this is a single line comment
''' 
this is a multi line comment
this is a multi line comment
this is a multi line comment
'''

# -----------------------------------
'''
short cut to open terminal in vs code is ctrl + j or 
ctrl + ` "`" this is called back tick you can find it below the esc key
'''

# -----------------------------------
# variable stores in a memory with a unique location 
# name = "Abdul Hannan"
# print(id(name)) # this will print the memory location of the variable name
# print(type(name)) # this will print the type of the variable name
# here type means the data type of the variable

# rules to define a variable name
# 1. variable name should not start with a number
# 2. variable name should not start with a special character except _ (underscore)  
# 3. variable name should not contain any special character except _ (underscore)
# 4. variable name should not be a keyword (reserved word) in python (like if, else, print , id, etc.)
# 5. variable name should not contain any space
# best practice to use snake case means all letter should be in lower and for seprate the words with _ (underscore)
# ------------------------------------

'''
type casting 
1. implicit type casting :python auto convert one data type to another data type
2. explicit type casting : user can convert one data type to another data type
by using the built in functions like int(), str(), float(),etc
'''
# ------------------------------------
# operators in python 
# Arithmetic Operators
# Comparison Operators
# Logical Operators
# Assignment Operators

# Arithmetic Operators
# + - * / % // **
# c = a - b
# c = a * b
# c = a / b
# c = a % b
# c = a // b
# c = a ** b # 10^3 = 10*10*10
# a = 10
# b = 3
# print(10 + b - 2 * a + 10)
#     10 + 3    -20  + 10
#     10 + 3        -10
#        3

# Comparison Operators
# == != > < >= <=
# a = 10
# b = 10
# c = a == b
# c = a != b
# c = a > b
# c = a < b
# c = a >= b
# c = a <= b
# print(c)

# logical Operators

# logical "and" operator 
# here output only be true if both condition are true 
# age = 25
# has_license = True

# Can drive if age is 18+ AND has license
# can_drive = age >= 18 and has_license
# print(can_drive)  # Output: True

'''
logical "or" operator
here output will be true if any one condition is true
hungry = True  
thirsty = False  

if hungry or thirsty:  
    print("Let's get a snack or drink! 🍔🥤")  
else:  
    print("I'm full! 😊") 
 '''
# logical "not" operator
# here output will be true if condition is false and vice versa
'''
is_weekday = False  

if not is_weekday:  
    print("It's the weekend! 🎉")  
else:  
    print("Work mode... 😴")  '''
# Assignment Operators
# = += -= *= /= %= //= **=
# a = 10
# b = 20
# a += b 
# a -= b 
# a *= b 
# a /= b  
# a %= b 
# a //= b 
# a **= b 
# print(a)


# ------------------------------------
# # if, else and elif statement

# taking user input and using it with if-else statement
# age = int(input("Enter your age: "))
# if   age > 18:
#          print("You are allowed.")
# elif age == 18:
#          print("Congrats on turning 18! You're just allowed!")
# else:
#         print("You are not allowed.")

