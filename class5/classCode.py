# def sum (a, b):
#     return a + b

# print(sum(1, 2))
# assingment

food_calories = {
    "biryani": 50,
    "pizza": 100,
    "burger": 150,
    "meat" : 200,
    "chicken": 250,
    "fish": 300,
    "vegetable": 350,
    "fruit": 400,
    "egg": 450,
}

def check_calories():
    favFood1 = input("Enter the food item: ").lower()
    
    def get_calories(food):
        if food in food_calories:
            return food_calories[food]
        else:
            return "Food not found"
    
    # Print the calories for the first food item
    food1 = get_calories(favFood1)
    if food1 == "Food not found":
        print("food not found try diffrent one")
    else:
        print(f"The calories in {favFood1} are {food1}")
    
    while True:
        question = input("Do you want to check the calories for another food? (yes/no): ").lower()
        if question == "yes" or question == "y":
            favFood2 = input("Enter another food item: ").lower()
            food2 = get_calories(favFood2)
            if food2 == "Food not found":
                 print("food not found try diffrent one")
            else:
                print(f"The calories in {favFood2} are {food2}")
        elif question == "no" or question == "n":
            print("Thank you for using the calorie checker!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

check_calories()

#  the following code is same in logic but different in syntax
# def sum(a, b):
#     return a + b

# sum = lambda a, b: a + b
# print(sum(1, 2))

