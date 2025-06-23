#!/usr/bin/python3

password = ""
timesIntered = 1
length = 0
while password != "secret123":
    password = input("Enter password: ")
    for i in password:
        length = length +1
    if password == "secret123":
        print("Access granted.")
    elif timesIntered % 3 == 0:
        print("Retry alert you seem to not remember your own password")
        timesIntered = timesIntered + 1
    elif length < 8:
        print("Error Too short.")
    elif not any(c.isdigit() for c in password):
        print("Error: Need a digit.")
        timesIntered = timesIntered + 1
    else:
        print("Access denied.")
        timesIntered = timesIntered + 1
