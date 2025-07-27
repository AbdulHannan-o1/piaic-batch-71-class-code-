# ===========================
# Object Oriented programming 
# ===========================
'''
class House:
    def __init__(self, address):
        self.address = address
        self.number_of_rooms = 4
        self.number_of_doors = 2
    def rang_the_bell(self):
        print("Ding Dong")

h1 = House("A302")
h2 = House("A202")
h3 = House("A102")

# print(h1.address)
# h1.rang_the_bell()
# print(h2.address)
# print(h3.address)

class Apartment(House):
    def __init__(self,addr, flat_numb):
        super().__init__(addr)  # bu using supper we can cacess the properties of its parent child 
        self.flat_number = flat_numb
    
aprt1 = Apartment("xyz",302)
print(aprt1.flat_number)
print(aprt1.address)
print(aprt1.number_of_doors)


class Student:
    def __init__(self): 
'''

# build a class of student with multiple classee and method 
# remaing code on the collab note book 
# Link :
# https://colab.research.google.com/drive/1acbhwNamJRuYoCal57Snqy6DoA6LEgp0?usp=sharing
