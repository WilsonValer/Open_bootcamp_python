#!/usr/bin/python3
year = int(input("Ingrese el Año: "))
def checkYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Is Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Is  Leap Year")
    else:
        print("Not a Leap Year")

checkYear(year)
