def main():
    userInput = input("Greeting: ").strip().lower()
    print(f"${value(userInput)}")


def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h") and greeting != "hello":
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
