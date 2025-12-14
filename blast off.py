def countdown():
    number = int(input("Enter a number to start the countdown:  "))

    for i in range(number, -1, -1):
        if i > 0:
            print(i)
        elif i == 0:
            print("BLAST OFF!!")

countdown()