marks = int(input("What is your score? "))

if marks > 90:
    print("Grade A")
elif marks >80 and marks <=90:
    print("Grade B")
else:
    print("Grade C")

name = input("What is your name? ")

match name:
    case "jai":
        print("Son")
    case "sindhu":
        print("Mother")
    case "mohan":
        print("Father")
    case _:
        print("Who?")
