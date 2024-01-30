x, y, z = input("Expression: ").split(" ")

if y == "+":
    print(float(x)+int(z))
elif y == "-":
    print(float(x)-int(z))
elif y == "*":
    print(float(x)*int(z))
elif y == "/":
    print(float(x)/int(z))
