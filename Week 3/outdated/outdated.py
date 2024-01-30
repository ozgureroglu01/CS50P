
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        user_date = input("Date: ")
        if "/" in user_date:
            month,day,year = user_date.strip().split("/")
            if int(month) > 12 or int(day)>31:
                continue
            date = f"{year}-{str(month).zfill(2)}-{day.zfill(2)}"
            break
        else:
            if "," not in user_date:
                continue
            month,day,year = user_date.replace(",","").split()
            if int(day)>31 :
                continue
            new_month = months.index(month)+1
            date = f"{year}-{str(new_month).zfill(2)}-{day.zfill(2)}"
            break
    except ValueError:
        pass

print(date)
