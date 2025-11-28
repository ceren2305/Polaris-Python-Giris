#Ask user for their name 
name = input("What is your name? ")

#Ask user for their age
age = int(input(f"How old are you {name}? "))

difference = 100 - age

year = 2025 + difference

print(f"You will turn 100 in the year {year}.")