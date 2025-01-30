import sys

def main():
    num = int(input("Give a number: "))
    print(square(num))
    print(sys.path)

def square(num):
    return num ** 2

if __name__ == "__main__":
    main()