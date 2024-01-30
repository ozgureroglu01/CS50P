
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
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
    return final_fuel


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{str(percentage)}%"


if __name__ == "__main__":
    main()
