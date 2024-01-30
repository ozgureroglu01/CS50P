import sys
import csv
from tabulate import tabulate


if len(sys.argv) == 2 and ".csv" in sys.argv[1]:
    try:
        pizza = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                pizza.append({"name": row[0], "Small": row[1], "Large": row[2]})



    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")


print(tabulate(pizza[1:], headers = pizza[0] , tablefmt="grid"))
