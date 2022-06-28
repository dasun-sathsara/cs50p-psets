
def get_input(prompt):
    while True:
        MENU = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }

        try:
            return MENU[input(prompt).title()]
        except KeyError:
            pass
        except EOFError:
            return None


total = 0
while True:
    item = get_input("Item: ")

    if item == None:
        break

    total += item
    print(f"Total: ${total:.2f} \n")
