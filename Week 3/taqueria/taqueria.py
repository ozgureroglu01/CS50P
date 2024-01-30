menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        order = input("Item: ").title()
        if order in menu:
            total += menu[order]
            print("Total: "+"$"+str("{:.2f}".format(total)))
    except (EOFError,KeyError):
        print()
        break
