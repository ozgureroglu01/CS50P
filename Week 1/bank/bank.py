userInput = input("Greeting: ").strip().lower()
if "hello" in userInput:
    print("$0")
elif userInput.startswith("h") and userInput != "hello":
    print("$20")
else:
    print("$100")

