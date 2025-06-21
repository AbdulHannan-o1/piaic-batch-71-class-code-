print("pakistan Zindabad")
# for the ompilation of the .py file 
#  python -m compileall {file name} 


'''
what is dis ?
'''
# a dis function dissaseemble the logic of the code 
import dis

def greet(name: str, age:int) :
    print(f"Hello, I am {name} and i am {age} year old ")

greet("Abdul-Hannan", 18)

dis.dis(greet)
# output  look like this 

'''
Hello, I am Abdul-Hannan and i am 18 year old 
 12           RESUME                   0      

 13           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST               1 ('Hello, I am ')
              LOAD_FAST                0 (name)
              FORMAT_SIMPLE
              LOAD_CONST               2 (' and i am ')
              LOAD_FAST                1 (age)
              FORMAT_SIMPLE
              LOAD_CONST               3 (' year old ')
              BUILD_STRING             5
              CALL                     1
              POP_TOP
              RETURN_CONST             0 (None)

'''