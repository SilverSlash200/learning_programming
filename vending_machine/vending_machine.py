def input_validation(user_val, lower_val, upper_val):
    while user_val not in range(lower_val, upper_val):
        try:
            user_val = int(user_val)
        except:
            user_val = input("Please enter a number! \n>")
            print()

def menu_items(list_name):
    print( "+------------------------------------+") # 38 Total
    print(f'| 0. Return / Back                   |')
    for i in range(len(list_name)):
        offset = 27 - len(list_name[i].name) - len(str(list_name[i].price))
        print(f'| {i + 1}. {list_name[i].name} - ${list_name[i].price}{" " * offset} |')
    print( "+------------------------------------+")
    
    # Item
    user_choice = input(f'Which item would you like?(0 - {len(list_name)})\n> ')
    print()
    
    # Input Validation
    user_choice = input_validation(user_choice, 0, len(list_name))
    
    # Exit menu
    if int(user_choice) == 0:
        return 0
    
    # User choice is human readable, array is 0 index
    user_choice -= 1
    
    # Quantity
    user_num = int(input(f'How many of {list_name[user_choice].name} would you like? \n> '))
    
    # Input Validation
    user_num = input_validation(user_num, 1, float('inf'))        
        
    user_purchase_list.append(list_name[user_choice])
    user_purchase_list[len(user_purchase_list) - 1].num = user_num
    
    return user_choice

class vending_item:
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc
        self.num = 0

# Drinks List
drinks_list = [None] * 9
drinks_list[0] = vending_item("Water",           0.25, "bottle water")
drinks_list[1] = vending_item("Coca-Cola",       1.25, "12oz can of Coke")
drinks_list[2] = vending_item("Sprite",          1.25, "12oz can of Sprite")
drinks_list[3] = vending_item("Mellow Yellow",   1.25, "12oz can of Mellow Yellow")
drinks_list[4] = vending_item("Dr. Pepper",      1.25, "12oz can of Dr. Pepper")
drinks_list[5] = vending_item("Red Gatorade",    1.00, "20oz bottle of Gatorade")
drinks_list[6] = vending_item("Blue Gatorade",   1.00, "20oz bottle of Gatorade")
drinks_list[7] = vending_item("Purple Gatorade", 1.00, "20oz bottle of Gatorade")
drinks_list[8] = vending_item("Orange Gatorade", 1.00, "20oz bottle of Gatorade")

# Drinks List
snacks_list = [None] * 4
snacks_list[0] = vending_item("Lays Chips",             1.00, "bags of Lays Chips")
snacks_list[1] = vending_item("Pringles Chips",         1.00, "can of Pringles")
snacks_list[2] = vending_item("Peanut Butter Crackers", 1.00, "package(s) of 6 peanut butter crackers")
snacks_list[3] = vending_item("Cheese Crackers",        1.00, "package(s) of 6 cheese crackers")

candy_list = [None] * 7
candy_list[0] = vending_item("Pay Day",    1.50, "payday bar")
candy_list[1] = vending_item("Skittles",   1.50, "package(s) of Skittles")
candy_list[2] = vending_item("Reese's",    1.50, "package(s) of Reese's")
candy_list[3] = vending_item("Twix",       1.50, "package(s) of Twix")
candy_list[4] = vending_item("Almond Joy", 1.50, "Almond Joy")
candy_list[5] = vending_item("Star Burst", 1.50, "package(s) of Star Burst")
candy_list[6] = vending_item("Honey Bun",  1.50, "Honey Bun")

# Main Vars
cont = True
user_purchase_list = []
running_total = 0.0

print("Welcome to the Vending Machine")

# Loop over the actual machine, this will be the 'rewrite' portion later
while cont:
    print("What Secion would you like to buy from?")
    print("+-------------+")
    print("| 1. Drinks   |")
    print("| 2. Snacks   |")
    print("| 3. Candy    |")
    print("| 4. Exit     |")
    print("+-------------+")
    
    user_category = input("Pick a Category:\n> ")
    print()
    
    # Input Validation
    user_category = input_validation(user_category, 1, 4)  
    print(user_category) 
    
    match int(user_category):
        case 1:
            user_choice = menu_items(drinks_list)
            print(user_choice)

        case 2:
            user_choice = menu_items(snacks_list)

        case 3:
            user_choice = menu_items(candy_list)

        case 4:
            cont = False

        case _:
            print("BROKEN, Exiting Now")
            break
    
    if user_category != 4 and user_choice != 0:
        user_cont = input("\nDo you want to continue ordering? (Y/n)\n> ")
        if user_cont == 'n':
            cont = False
    
    if user_choice != 0:
        print("\n--------------------------------------\n")
        print("\tYou bought the following: \n")
        for i in range(len(user_purchase_list)):
            print(f'\t  {user_purchase_list[i].name}: {user_purchase_list[i].num} @ {user_purchase_list[i].price}')
            line_total = int(user_purchase_list[i].num) * float(user_purchase_list[i].price)
            print(f'\n\t  Item total: ${line_total}')
            running_total += line_total
        print("\n--------------------------------------\n")

print(f'Your total is: ${running_total}')
