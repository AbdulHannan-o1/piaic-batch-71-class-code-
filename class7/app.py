'''
==========================
What are Callback function
==========================
'''
# calling a funcrion inside a function without using decoretor 
#They are also knows as callback function
''' 
def fun1(fun2, func3):
    print("hello")
    fun2()
    func3()

def fun2():
    print("world")

def func3():
    print("It's Team Random")

fun1(fun2 , func3)
#note 
'''
'''
if we call a function like this
print(func1)  
the output will be none if we are not  using return statmenet in the function 
if the return statment is used the output shows the rrturn value 
'''


''''
====================
what are decorator ?
====================
Ans: an advanced method to call and run  function inside a function 
'''
# def greating (func):
#     def wrapper():
#         print("before calling the dunction")
#         func()
#         print("after calling the function")

#     return wrapper

# @greating
# def greet():
#     print("Hello! World")
    
# greet()

'''
==================================
example for the decorator function
================================== 
'''

# def auth_checker(fun):
#     def wrapper():
#         user = "logged in!"
#         if (user == "logged in!"):
#             print("checking for authentication....")
#             fun()
#         else :
#             print("log in first to get access to your portal ")
#     return wrapper


# @auth_checker
# def access_dashboard():
#     print("you are logged in and accessed dahshbord")

# @auth_checker
# def get_addmission():
#     print("you can get the addmission")


# access_dashboard()
# get_addmission()


'''
===============
What are Loops?
===============
'''
# ---------
# for Loops
# ---------
# serial = 1
# nameOfStudents = ["okasha", "ALi", "Hamza" , "Azfar"]
# for name in nameOfStudents  :
#     print(f" {serial}. {name}")
#     if name == "Hamza":
#         break         #here the loop breaks as soon as the loop encounter "Hamza"it means that loop didnot print "Azfar"
#     serial += 1

# ----
# task
# ----
'''
printing numbers from 1 till 100 using for loop
'''
# for i in range(1,10) : 
#     print(i)

'''
printing table of 2 by using for loop
'''
# root_list = []
# #         start    stop    step
# for i in range(2   ,     11    , 2):
#     root_list.append(i)

# print(root_list)

# list comprehension 
# new_list = [numb**2 # here we are squaring the numbers between 1 and 10 and storing only the even numbers
#             for numb in range(1,11)
#               if numb% 2 == 0 
#             ]
# print(new_list)

#list comperision whith string 
# upper_case = [ names.upper() for names in nameOfStudents]
# print(upper_case)

# ----------
# while Loop
# ----------
# guess the number game
