import random


def main():
    level = get_level()
    count = 0
    score = 0
    while count < 10:
        inner_count = 1
        x,y = generate_integer(level)
        result = x + y
        question = f"{x} + {y} = "
        answer = input(question)
        while inner_count < 3:
            if int(answer) == result:
                score += 1
                break
            else:
                print("EEE")
            answer = input(question)
            inner_count += 1
        if inner_count == 3:
            print(question + str(result))
        count += 1
    print(f"Score: {score}")

def get_level():
    level = input("Level: ")
    while level not in ["1","2","3"] or level.isdecimal() == False:
        level = input("Level: ")
    return int(level)


def generate_integer(level):
    if level == 1:
        random_integer_x = random.randint(0,9)
        random_integer_y = random.randint(0,9)
    elif level == 2:
        random_integer_x = random.randint(10,99)
        random_integer_y = random.randint(10,99)
    elif level == 3:
        random_integer_x = random.randint(100,999)
        random_integer_y = random.randint(100,999)
    else:
        raise ValueError
    return random_integer_x,random_integer_y


if __name__ == "__main__":
    main()
