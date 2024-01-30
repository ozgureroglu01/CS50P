def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return first_two_letter(s) and  contains_more(s) and size(s) and numbers(s)


def first_two_letter(s):
    return True  if s[:2].isalpha() else False

def contains_more(s):
    return s.isalnum()

def size(s):
    return True if 2 <= len(s) <= 6 else False


def numbers(s):
    i = 0
    while i < len(s)-1 :
        if s[i].isdigit() and i>0:
            if s[:i].isalpha():
                if s[i] == "0":
                    return False
                break
        i+=1
    if s[i:].isdigit() or s.isalpha():
        return True
    return False


main()
