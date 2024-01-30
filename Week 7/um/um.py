import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count_list = re.findall(r"\bum\b",s, flags=re.IGNORECASE)
    return len(count_list)


if __name__ == "__main__":
    main()
