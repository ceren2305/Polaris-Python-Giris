#Ask user for their exam result
result = int(input("What is your exam result? "))

if result > 50:
    print("You passed")
if result < 50:
    print("You failed")