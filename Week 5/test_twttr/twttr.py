def main():
    word = input("Input: ")
    output = shorten(word)
    print("Output: "+ output)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A","E","I","O","U"]

    words = []
    for letter in word:
        words.append(letter)

    non_vowels = []
    for i in words:
        if i not in vowels:
            non_vowels.append(i)

    new_word = "".join(non_vowels)
    return new_word


if __name__ == "__main__":
    main()
