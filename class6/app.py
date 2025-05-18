# data  types 
# in old python 
'''
first_name = "John"
'''
'''
# in newer version 
first_name: str = "Abdul Hannan"    # here :str defines the data type of the value
age: int = 25  #using for int 
is_student: bool = True  #using for boolean
height: float = 5.9    #using for float
# list
fruits: list[str] = ["apple", "banana", "cherry"]  #using for list here
# :list defines the whole data in list as a list and [str] uses to define the data of string is string 

# data types for function 
def greet(name: str, age: int) -> str:
    return f"Hello, {name} and your age is {age}!"
# here name:str defines the data type of name parameter 
# and ->str defines the data type of return (means the type of value that function will return  )

message = greet("Abdul Hannan", 25)
print(message)  # Output: Hello, Abdul Hannan and your age is 25!
'''

'''
camel case 
in camel case the first letter of the first word is small and the first letter of the second word is capital
rollNo
'''

# dictonaries 
"""
studentDetails = {
    "name": "Abdul Hannan", # here name is key and Abdul Hannan is value
    "age": 25,  # here age is key and 25 is value
    "rollNo": 12356, # here rollNo is key and 12356 is value
    "address": "karachi"   # here address is key and karachi is value
}

print(studentDetails)  # Output: {'name': 'Abdul Hannan', 'age': 25, 'rollNo': 12356, 'address': 'karachi'}
# this approach will print hte whole dictionary
print(studentDetails["name"])  # Output: Abdul Hannan
# this approach will print the value of key name
print(f'''
    Name= {studentDetails["name"]}
    Age = {studentDetails["age"]}
    Roll No= {studentDetails["rollNo"]}
''')


for key, value in studentDetails.items():
    print(f"{key.capitalize()}= {value}") 
    if key == "rollNo":
        break
"""

def llm(promt:str) ->str:
    return {
        "content": "Hello, how can I help you?",
        "role": "assistant"
    }

result = llm("hi")
