#! /usr/bin/env python3

def fizzBuzz(i):
    if i%3 == 0 and i%5 == 0:
        return "FizzBuzz"
    elif i%3 == 0:
        return "Fizz"
    elif i%5 == 0:
        return "Buzz"
    else :
        return str(i)

def main():
    for i in range(1, 101):
        print(fizzBuzz(i))


if __name__ == "__main__":
    main()