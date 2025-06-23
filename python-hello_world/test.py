#!/usr/bin/python3

while True:
    try:
        message = input("Enter a number: ")
        number = int(message)
        for i in range(1, number, 1):
            print(f"{i}*{number} ={i * number}")
    except ValueError:
        print("please enter entegers only")
