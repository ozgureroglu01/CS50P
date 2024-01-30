while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        while x > y:
            fraction = input("Fraction: ")
            x = int(x)
            y = int(y)
            fuel = (100/y)*x
            final_fuel = round(fuel)
        fuel = (100/y)*x
        final_fuel = round(fuel)
        break
    except (ValueError, ZeroDivisionError):
        pass


if final_fuel <= 1:
    print("E")
elif final_fuel >= 99:
    print("F")
else:
    print(str(final_fuel)+"%")
