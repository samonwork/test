"""
print("Childcare service!")

pName = input("Enter child's name: ")
pAge = input("Enter child's age: ")

try:
    pAgeInt = int(pAge)

    Kindergarten_min_age = 4

    if pAgeInt >= Kindergarten_min_age:
        if pAgeInt < 12:
            print(f"{pName} can attend kindergarten!")
        else:
            print(f"{pName} is too old for kindergarten.")
    else:
        print(f"{pName} is too young for kindergarten.")
except ValueError:
    print("Invalid age. Please enter a valid age as a number.")

"""

"""

def input_function():
    iText = input("Enter text: ")
    rText = return_function(iText)
    final_function(rText)

def return_function(iText):
    tText = iText + " too!"
    return tText

def final_function(fText):
    print(fText)

input_function()

"""

x=0
while (x<5):
    print(x+1)
    x=x+1
y=0
for y in range(5,10):
    print(y+1)

days=["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
for d in (days):
    if d.startswith("T"):
        print(d)  
