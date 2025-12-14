while True:
    try:
#Ask user for a value of x
         x = int(input("What is x? "))
    except ValueError:
        print("x is not a valid value, please enter a valid value.")
    else:
        break

print(f"x is {x}")