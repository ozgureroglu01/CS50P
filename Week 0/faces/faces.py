def main():
    userInput = input()
    print(convert(userInput))

def convert(userInput):
    userInput = userInput.replace(":)", "🙂")
    userInput = userInput.replace(":(", "🙁")
    return userInput


main()
