vowels = ["a", "e", "i", "o", "u", "A","E","I","O","U"]
user_input = input("Input: ")
words = []
for letter in user_input:
    words.append(letter)

non_vowels = []
for word in words:
    if word not in vowels:
        non_vowels.append(word)

new_word = "".join(non_vowels)
print("Output: "+ new_word)
