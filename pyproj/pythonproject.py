import datetime
stringnr = input("Enter year of birth: ")

try:
    if int(stringnr) >= 1900:
        print(f'You were born {datetime.date.today().year - int(stringnr)} years ago.')
    else:
        print("You're dead!")

except Exception:
    print("Invalid value!")