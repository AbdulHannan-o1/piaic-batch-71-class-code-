'''
def age_checker(age: int)-> bool:
    return

result = age_checker("18")
'''
# print(result)
# by default using type hint as int while the type of argument is string python doesn't throw an error by default 
# to throw the error we can use the third party pakage mypy
'''
name = "hello"
print(id(name))
name= "world"
print(id(name))
print(id(2881434794480))
# in this case for same variable name but with diffrent value python creates new variable for it and remove the previous one

# set
roles = {"admin", 2,1,5, "Hello"}

roles.update("admin")
print(roles)

traffic_light:frozenset = frozenset({"red", "Yellow", "Green"})
# traffic_light.add("blue")  
# incomment to see the error
# beouse frozenset is immutable
'''
'''
print("///////////////////////////")
a= 90
b=a
a = 40
print(b) #output = 90 /// beocuse any type of varirable is immutable 

print("///////////////////////////")
print("======================")
name = ["a","b","c"]
new_name = name
name[0] = "z"
print(new_name[0])  #output is z beause list are mutable and the value storted in list are mutable 
print("=====================")
'''
# ==========================
# shorter syntax for if-else 
# ==========================
'''
admission_status = True

result = "you are allowed " if admission_status == True else "you are not allowed"
print(result)
'''
