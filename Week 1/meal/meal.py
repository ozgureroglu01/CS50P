def main():
    time = input("What time is it? ")
    newTime = convert(time)
    if 7.0<=newTime<=8.0:
        print("breakfast time")
    elif 12.0<=newTime<=13.0:
        print("lunch time")
    elif 18.0<=newTime<=19.0:
        print("dinner time")


def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = int(minutes)
    return (hours*60+minutes)/60





if __name__ == "__main__":
    main()
