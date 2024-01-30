import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    if match := re.search(r"^" + regex + " to " + regex + "$", s):
        start_time =time_convert(match.group(1), match.group(2), match.group(3))
        end_time = time_convert(match.group(4), match.group(5), match.group(6))
        return f"{start_time} to {end_time}"
    else:
        raise ValueError


def time_convert(hours,min,meridiem):
    if hours == "12":
        if meridiem == "AM":
            hours = "00"
        else:
            hours = "12"
    else:
        if meridiem == "PM":
            hours = f"{int(hours)+12}"
        else:
            hours = f"{int(hours):02}"
    if min == None:
        min = "00"

    else:
        min = f"{int(min):02}"
    return f"{hours}:{min}"


if __name__ == "__main__":
    main()
