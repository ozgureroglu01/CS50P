from datetime import date
import sys
from datetime import datetime
import inflect


def main():

    birthdate = get_date().date()
    current_date = date.today()
    print((get_diffrence_in_text(birthdate,current_date)))

def get_date():
    birthtime = input("Date of Birth: ")
    if validate_date(birthtime):
        return datetime.strptime(birthtime,"%Y-%m-%d")
    else:
        sys.exit("Invalid date")


def validate_date(d):
    date_format = "%Y-%m-%d"
    try:
       return bool(datetime.strptime(d,date_format))
    except ValueError:
        return False


def get_diffrence_in_text(birthdate,current_date):
    p = inflect.engine()
    diffrence = current_date - birthdate
    diffrence_in_minutes = round(diffrence.total_seconds() / 60)
    return f'{p.number_to_words(diffrence_in_minutes,andword="")} minutes'.capitalize()




if __name__ == "__main__":
    main()
