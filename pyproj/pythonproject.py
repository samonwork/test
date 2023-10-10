import datetime
stringnr = input("Enter year of birth: ")

try:
    if int(stringnr) >= 1900 and int(stringnr) <= datetime.date.today().year:
        print(f'You were born {datetime.date.today().year - int(stringnr)} years ago.')
    elif int(stringnr) > datetime.date.today().year:
        print("You're unborn!")
    else: 
        print("You're dead!")

except Exception:
    print("Invalid value!")