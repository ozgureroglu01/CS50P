userInput = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
userInput = userInput.lower().strip()
words = ["42","forty two","forty-two"]
if userInput in words:
    print("Yes")
else:
    print("No")
