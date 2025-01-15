def main():
    number = getNumber()
    repeatName(number,getName())

def getName():
    return input("What is your name? ")

def getNumber():
    while True:
        number = int(input("How many times? "))
        if number > 0:
            return number
        
def repeatName(number,name):
    for _ in range(number):
        print(name)

main()