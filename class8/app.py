'''
# parameter for print( a pre defined function )
print(1,2,3,4,5,sep='----') #output: 1----2----3----4----5
print(1,2,3,4,5,end='----') #output: 12345----
'''
'''
points to understand any type of program (for technical or non-technical)
it provides an easy way to understand the code for developer community
1. copy the code of any predefined function by pressing ctrl + click on the function name
2. copy the whole code of the function 
3. select the best LLM (deepseek will directly create a UML daigram)
4. The promt of (creat UML)  and past the code 
5. gerate the result and copy it 
6. go to the palntext editor and paste the result
7. A daigram will be genrated and anuone can understand it 
8. go to notebooklm and paste the ocde copyed form the function
9. This will creat a road map of the code 
'''        
'''
parameters and staric
songle staric means (*) it define unlimited positional argument 
double staric meand (**) unlimited key word argyments 
'''            
'''
genrator function 
genrates a number then check for the condition if true then stored in memory 
never run automaticaly 
remmrmber the last genrated number
you are genrating a itereation and in between work on diffrent thing
the genrator will remmber the genrated number 
'''
'''
With Block 
when we open a file we need to close it after use
with open('file.txt', 'w') as file:  # 'w' mode for writing
    file.write('Hello, World!')
here with block will automatically close the file after the block is executed
'''
# asynch and synchronous programming 
# asynchronous programing 
''''
import asyncio
import time 

startTime = time.time()
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    # Run both tasks in parallel
    await asyncio.gather(task1(), task2())

asyncio.run(main())

end = time.time()
print(f"total time : {end - startTime:.2f} second ")
'''
# ======================================
# Error Handling or execptional handling 
# =======================================
'''
three type of eror 
1. develpment time error
2. testing time error 
3. logical error (mens you write a function to add two numbers but use a -sign instead of + sign)this is called a logicla error 
4. production time error
'''
# developmet type error 
def myFunc(num1: int, num2: int)-> int:
    return num1 + num2 
    
#myFunc(1, '2') # this will raise a type error because we are passing a string instead of an integer

# usung try and except block to handle the error
# print("Before the error")
# try:
#     7 / 0 
# except ZeroDivisionError as e:
#     print(f"can nt divide a number by zero: {e}")
# except TypeError as e:
#     print(f"type error ")
# print("After the error")  # This line will not be executed due to the error above

'''
sppoose there are 10 error by the above code only one error will be printed
'''
# for dynamic error handling we can use the Exception class
try:
    # 7 / 0
    # print(7/0)
    int("AAAAA")
    print(name[0])
except Exception as e:
    print(f"An error occurred: {e}")
finally:        # this block will always run doen't matter if there is an error or not
    print("This block always executes, regardless of whether an error occurred or not.")