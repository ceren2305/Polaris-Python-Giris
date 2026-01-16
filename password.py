import re

def check_password_strength(password):

    #Regex Patterns:
    #(?=.*[A-Z]) :at least one uppercase letter
    #(?=.*\d) :at least one digit
    #(?=.*[@!%*?&.]) :at least one special character
    #[A-Za-z\d@!%*?&.]+ :Allowed character set

    regex_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@!%*?&.])[A-Za-z\d@!%*?&.]+$"

    if re.match(regex_pattern, password):
        return True
    else:
        return False
    
user_password = input("Create a password: ")

if check_password_strength(user_password):
    print("Strong Password")
else:
    print("Weak Password")