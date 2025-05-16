# using function to build a calculator

def calculate( ):
    output =0 
    num1 = int(input("enter 1st number\n"))
    num2 = int(input("enter 2nd number\n"))
    operator = input("enter the operator (+, -, *, /, %)\n")
    if operator not in ["+", "-", "*", "/" , "%"]:
        return "Invalid operator"


    if operator == "+":
        output =  num1 + num2
    elif operator == "-":
        output=  num1 - num2
    elif operator == "*":
        output =  num1 * num2
    elif operator == "/":
        output =  num1 / num2
    elif operator == "%":
        output =  num1 % num2
    else:
        return "Invalid operator"
    
    return output   
 # return also known as termination of function as the function encounter return statment the code below will not be executed
result = calculate()
# print(result)
def printf(result):
    print("The result is: ", result)

printf(result)



# # this function decide the discount based on the qyt of item
# def discount_func ():
#     qty_of_juicer = int(input("Enter the qty of juicer you want to buy \n"))
#     qty_of_blender = int(input("Enter the qty of blender you want to buy \n"))

#     if qty_of_juicer or qty_of_blender <= 5:
#         discount = 0
#         print("No discount available")
#     elif qty_of_juicer or qty_of_blender <= 10:
#         discount_on_qty = 5
#         return discount_on_qty
#     elif qty_of_juicer or qty_of_blender <= 20:
#         discount_on_qty = 10
#         return discount_on_qty
#     elif qty_of_juicer or qty_of_blender <= 30:
#         discount_on_qty = 15
#         return discount_on_qty
#     elif qty_of_juicer or qty_of_blender <= 50:
#         discount_on_qty = 20
#         return discount_on_qty
#     else:
#         print("No discount available or enter a valid qty")


# print(discount_func())


    




