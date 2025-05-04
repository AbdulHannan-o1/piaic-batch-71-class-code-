# built in function 
'''
first_name ="Hamza"
id() function  print the location of the variable 
print(id(first_name))
# type() fintion 
x =10     #output = int
x= 2.2    #output = float 
x= True   #output = bool
x= "Hamza" #output = str 
print(type(x))
'''
# .is digit function 
'''
my_age =  input("enter your age:")
if my_age.isdigit():
    print(my_age)
else:
    print("enter a valid age")
'''

# # Logical operator

# if conditions prints if both the conditions are true (using and operator)
'''
bobzi_runs = 10
total_bolls= 20
total_sizes = 5
#    here first and operator executes and then or operator executes
if bobzi_runs >= 50 and total_bolls < bobzi_runs or total_sizes >= 5:
    # false          and      false                  
    #            false                 or                true 
    #                                   true
    print("👑 king ")
else:
    print("🔔king ")
'''
# list 
# index starts from 0
#            0    ,   1     ,  2   ,   3
'''
grocery = ["milk", "eggs", "bread", "butter"]
print(grocery) # printing the items of list 

print(len(grocery)) # this will print the length of the list
print(grocery[0]) # this method allow us to print specific item of the list
dir(grocery) # dir functions will print all the possible methods or the operation that can be performed on the list
# .pop functions
grocery.pop() # this will remove the last item of the list
grocery.pop(0) # by passing the index number of the list we can removethe specific item of the list
# grpcery.pop(-1) here - sign means that it will count from the last item of the list

# append function add any thing to teh list 
grocery.append("sugar") # this will add the item to the end of the list

grocery.insert(3, "rooti") # this will add the item to the start of the list

grocery.remove("eggs")
print(grocery) # this will print the list after removing the last item of the list
'''

# class challenge
veg= ["gajar", "pyaz", "alu", "harimirch", "lalmirch"]
# veg.pop(-4)
# print(veg[0:2]) 
veg.pop(-3)
veg.append("Moli")
veg.insert(4, "began")
veg.remove("pyaz")
print(veg[1:3])
































# grocery = [
#     {"name": "milk", "qty": "1 liter"},
#     {"name": "eggs", "qty": "1 dozen"}
# ]