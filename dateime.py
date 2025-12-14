from datetime import datetime

def calculate_time_remaining():
    date_format = "%Y-%m-%d %H:%M:%S"

#Ask user for their next exams date
    print(f"When is your next exam? Please give the target time in the Year-Month-Day Hour:Minute:Second format: ")


    target_time_str = input("Target Date and Time: ")

    target_time = datetime.strptime(target_time_str, date_format)

#Get the current time
    current_time = datetime.now()

#Calculate the difference
    time_difference = target_time - current_time
    total_seconds = int(time_difference.total_seconds())

#Calculate Days, Hours, Minutes, Seconds

#Calculate Days
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)

#Calculate Hours
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

#Calculate Minutes
    minutes = remaining_seconds // 60

#Calculate Seconds
    seconds = remaining_seconds % 60

    print(f"Time Remaining Until the Exam: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

calculate_time_remaining()