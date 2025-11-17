#{"product": count}
inventory = {"tomato": 5, "cucumber": 7, "bread": 1}
print(inventory)

def add_product(inventory):
    while True:
        try:
            count = int(input("Enter a count of product you want to add: "))
            for i in range(count):
                key = input("Enter a product name: ").lower()
                value = int(input("Enter a count of product: "))
                if key in inventory:
                    inventory[key] += value
                else:
                     inventory[key] = value
            break
        except ValueError:
            print("Error! Enter a number")
    print(inventory)

def remove_product(inventory):
    answer = input("Do you want to remove a whole product? (y/n)").lower()
    if answer == "y":
        try:
            count = int(input("Enter a count of products you want to remove: "))
            for i in range(count):
                key = input("Enter a product name: ").lower()
                if key in inventory:
                    del inventory[key]
                else:
                    print("error")
            print(inventory)
        except ValueError:
            print("Error! Enter a number")
    else:
        try:
            count = int(input("Enter a count of products you want to remove: "))
            for i in range(count):
                key = input("Enter a product name: ").lower()
                if key in inventory:
                    value = int(input("How many items you want to remove? "))
                    inventory[key] -= value
                    if inventory[key] <= 0:
                        del inventory[key]
                else:
                    print("error")
        except ValueError:
             print("Error! Enter a number")

def change_product(inventory):
                item = input("Which product you want to change? ").lower()
                if item in inventory:
                    try:
                        count = int(input("How many items you want to change? "))
                        inventory[item] = count
                    except ValueError:
                        print("Error! Enter a number. The change was not applied.")
                else:
                    print(f"There's no {item} products.")

def exit_program(inventory):
    print("Program is done.")

while True:
    print("1. Add products")
    print("2. Remove products")
    print("3. Change products")
    print("4. Exit")
    try:
        question = int(input("enter a number: "))
        if question == 1:
            add_product(inventory)
        elif question == 2:
            remove_product(inventory)
        elif question ==3:
            change_product(inventory)
        elif question == 4:
            break
        else:
            print("error")
    except ValueError:
        print("Error! Enter a number")
