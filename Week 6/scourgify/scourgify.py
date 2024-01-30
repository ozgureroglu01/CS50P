import sys
import csv



if len(sys.argv) == 3 and ".csv" in sys.argv[1]:
    try:
        student_info = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_info.append({"name": row["name"], "house": row["house"]})

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for info in student_info:
                name = info["name"]
                last,first = name.split(",")
                house = info["house"]
                writer.writerow({"first":first.strip(),"last":last.strip(),"house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")


