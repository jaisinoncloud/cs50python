"""
try:
    n = int(input("Number? "))
except ValueError:
    print("Sorry not a valid integer")
except Exception as e:
    print("Sorry there is something wrong")
    print(e)

else:
    print(n**2)

try:
    new = n * 2

except NameError as e:
    print("sorry no assignment possible")
    print(e)
"""

def main():
    n = get_number("What number? ")
    print(f"Number is {n}")

def get_number(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            pass
            #print("Sorry not a number try again")
        else:
            return n

main()