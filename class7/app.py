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
import random
randomNumFOrEasy:int = random.randint(1,50)
randomNumFOrPro:int = random.randint(1, 100)

counter:int = 0

def easyMode() :
    global counter
    counter = 0
    while True:
        print("you are in easy Mode")
        userInput:int = int(input("Guess a number between 1-50\n "))
        if randomNumFOrEasy == userInput:
            print(f"Conratulation You Won 🏆\n")
            break
        else:
            print("better Luck Next Time \n")
            if randomNumFOrEasy < userInput:
                print("Your guess is TOO HIGH \n")
            elif randomNumFOrEasy > userInput:
                print("Your Guess is TWO Low \n")
            else:
                print("enter a valid number \n")
        counter += 1
        print(f"your remaing tries are {15-counter}")
        if counter == 15:
            print("You Loss 😂")
            break

# function for intermediate mode 
def interLevelMode() :
    global counter
    counter = 0 
    while True:
        print("You are in intermediate level\n")
        userInput = int(input("Guess a number between 1-100\n "))
        if randomNumFOrPro == userInput:
            print(f"Congratulation You Won 🏆\n")
            break
        else:
            print("better luck next time\n")
            if randomNumFOrPro < userInput:
                print("Your guess is TOO HIGH\n")
            elif randomNumFOrPro > userInput:
                print("Your Guess is TOO LOW\n")
            else:
                print("Enter a valid number\n")
        counter += 1
        print(f"your remaing tries are {10-counter}")

        if counter == 10:
            print("you Loss 😂")
            break

# function for advanve mode 
def advanMode() :
    global counter
    counter = 0 
    while True:
        print("you are in advance mode\n")
        userInput = int(input("Guess a number between 1-100\n "))
        if randomNumFOrPro == userInput:
            print("Congratulation You WOn 🏆\n")
            break
        else:
            print("Better luck next Time\n")
            if randomNumFOrPro < userInput:
                print("Your guess is TOO HIGH\n")
            elif randomNumFOrPro > userInput:
                print("Your Guess is TOO LOW\n")
            else:
                print("Enter a valid number\n")
        counter += 1
        print(f"your remaing tries are {5-counter}")
        if counter == 5:
            print("YOu Loss 😂\n")
            break

def guessGame() :
    level = input(('''
    Which level would you like to play ?
    1) Easy (20 tries with range of 1 till 50)
    2) Intermediate (10 tries with 1 till 100 range)
    3) Advance Mode (5 tries with  1 till 100 range)
     '''))
    print(level)
    if level == "easy" or level=="1" :
        easyMode()
    elif level == "intermediate" or level=="2":
        interLevelMode()
    elif level == "advance" or level=="3":
        advanMode()
    else:
        print("select a valid mode")


guessGame()
        

