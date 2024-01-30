grocery_dict = {}
while True:
    try:
        item = input().upper()
        if item not in grocery_dict:
            grocery_dict[item] = 1
        elif item in grocery_dict:
            grocery_dict[item] += 1
    except EOFError:
        break



for key in sorted(grocery_dict):
    print(f"{grocery_dict[key]} {key}")


