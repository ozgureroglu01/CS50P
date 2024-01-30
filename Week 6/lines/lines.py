import sys

line_count = 0
if len(sys.argv) == 2 and ".py" in sys.argv[1]:
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        for line in lines:
            line = line.lstrip()
            if line.startswith("#") or len(line) == 0:
                continue
            line_count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_count)

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")




