user_ınput = input("camelCase: ")
word = []
for letter in user_ınput:
    if letter.isupper():
        word.append(" ")
    word.append(letter)
new_word = "".join(word)
new_word = new_word.replace(" ", "_")
print("snake_case: " + new_word.lower())
