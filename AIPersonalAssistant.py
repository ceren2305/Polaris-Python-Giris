class Assistant:
    def __init__(self, name):
#Initial Attributes
        self.name = "cero6"
#Hidden from the user and always starts at 0
        self.process_count = 0

    def greet(self, username):
#Increment process_count by 1 each time it runs
        self.process_count += 1
        print(f"Hello {username}, I am {self.name}. How are you today {username}? Shall I help you {username}? or Do you just want to talk {username}?")

    def status_report(self):
        print(f"I have performed a total of {self.process_count} operations so far.")

#TEST

#Create the assistant with the name "cero6"
my_assistant = Assistant("cero6")

#Greet "Ceren"
my_assistant.greet("Ceren")
my_assistant.greet("Ceren")
my_assistant.greet("Ceren")
my_assistant.greet("Ceren")

#Check the process count
my_assistant.status_report()