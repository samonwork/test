import random

secret_number = random.randint(1, 9)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You lost!")

"""
stringnr = input("Enter year of birth: ")
try:
    if int(stringnr) >= 1900 and int(stringnr) <= datetime.date.today().year:
        print(f'You were born {datetime.date.today().year - int(stringnr)} years ago.')
    elif int(stringnr) > datetime.date.today().year:
        print("You're unborn!")
    else: 
        print("You're dead!")

except Exception:
    print("Invalid input!")

"""