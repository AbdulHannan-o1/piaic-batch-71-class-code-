# ------------------
# What are modules ?
# ------------------

'''
large set of code jis may ,ultiple funtions ho os ko multiple may break karna or os ko main file may import kary gy 
jis say code zyada readable or understandable ho jata hay 
agar koi module kisi or folder may hay to os ko import karnay kay liye
folder ka name .or file ka name  use hota hay like this ( from module.payFee import payFee)

pypi.org python ka package index hay jahan say hum packages download kar sakty hain

python create a virtual enviroment and all the module you install the store in the VE (virtual enviroment)
and when ever you try to import a module python look in the ve 
module in VE are the global module so any project can be use in your system no need to install it again and againk
'''
# from auth import login, logout
# import auth
# from module.payFee import payFee

# print("before login")
# # login("abc", "abc")
# auth.login("abc", "abc")
# print("after login")

# print("before pay fee")
# payFee()
# # logout()
# auth.logout()



# =======================
# what is file handling ?
# ========================
# must create a random quote generator using an api
# to perform any type of function on data in a file we use pandas of openAi SDK they can genrate smmary nad many other things can be done 

# with key workd hepls us to open and close thec file automaticaly if we use manul approach 
# we are suppose to open and close file manuly whih ause error if file is not losed  

#                       w+ it allow us to  read and write at the same time
with open( 'text.txt' ,'w')as file :
    file.write("hello World")
    

'''
diffrence of read and write 
in w+ if file does not exits it creats a file and perform the operation on it 
while in r+ if file does not exist it throus error 
'''

# =============
# List & Tuples 
# =============

''''
to store multiple items in a single variable list are use [] these bracktets are use in list
while in tuples we use () or it works with out bracket but sepration with comma is permenent
in list we can add rermove and perform any action on the items on the otherhand in tuple we an not edit the
items 
'''
fruitList = ["apple","banana"] #ex of list 

fruitTuple = "apple", "banana"   # ex of tuple 


# ====
# set
# ====

'''
set doesnt allow duplicates 
it is an unordered list 
'''

roles = {'admin', 'student', 'teacher', 'student'}
print(roles)