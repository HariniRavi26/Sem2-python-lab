#1.
class User:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.email = ""
        self.n = 0

    def validate_name(self, name):
        special_characters = "!@#$%^&*()-+?_=,<>/{}[]|"
        num_count = sum(char.isdigit() for char in name)
        special_count = sum(char in special_characters for char in name)

        if num_count == 1 and special_count == 1:
            return True
        else:
            print("Invalid name! Must contain exactly one number and one special character.")
            return False

    def validate_password(self, password):
        if len(password) > 8:
            print("Invalid password! Should not be greater than 8 characters.")
            return False
        
        allowed_specials = "#_@"
        for char in password:
            if not char.isalpha() and char not in allowed_specials:
                print("Invalid password! Must not contain numbers or special characters (except #, _, @).")
                return False
        return True

    def validate_email(self, email):
        if "@" in email and "." in email and email.index("@") < email.index("."):
            return True
        else:
            print("Invalid email format! Please enter a valid email.")
            return False


    def get_user_input(self):
        while True:
            name = input("Enter your Name: ")
            if self.validate_name(name):
                self.name = name
                break
        
        while True:
            password = input("Enter your Password: ")
            if self.validate_password(password):
                self.password = self.validate_password(password) 
                break

        while True:
            email = input("Enter your Email Address: ")
            if self.validate_email(email):
                self.email = email
                break

        while True:
            try:
                self.n = int(input("How many times do you want to Print? "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def display_output(self):
        print(f"\n{self.name} wants to print {self.n} times and send mail to {self.email}.")
        print(f"Your password {self.password} will be encrypted and stored.")

user = User()
user.get_user_input()
user.display_output()

#2.
class PasswordRecovery:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.password = ""
        self.security_q1 = "What is your favorite color?"
        self.security_q2 = "What is your birth month?"
        self.answer1 = ""
        self.answer2 = ""

    def validate_password(self, password):
        if len(password) > 8:
            print("Invalid password! Should not be greater than 8 characters.")
            return False

        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in "!@#$%^&*()-+=<>?/{}[]|" for char in password)

        if has_digit and has_special:
            return True
        else:
            print("Invalid password! Must contain at least one number and one special character.")
            return False

    def get_user_details(self):
        self.name = input("Enter your Name: ")
        self.department = input("Enter your Department: ")

        while True:
            password = input("Enter your Password: ")
            if self.validate_password(password):
                self.password = password
                break

        while True:
            retype_password = input("Re-Type your Password: ")
            if retype_password == self.password:
                print("Password confirmed successfully!\n")
                break
            else:
                print("Passwords do not match! Try again.")

    def password_recovery(self):
        print("\nForgot Password? Answer Security Questions")

        while True:
            ans1 = input(f"{self.security_q1} ")
            ans2 = input(f"{self.security_q2} ")

            if ans1.lower() == self.answer1.lower() and ans2.lower() == self.answer2.lower():
                print(f"\nYour Password is: {self.password}")
                break
            else:
                print("Incorrect answers! Try again.")

    def password_verification(self):
        attempts = 3
        while attempts > 0:
            entered_password = input("Enter your Password: ")
            if entered_password == self.password:
                print("\nLogin successful!")
                return
            else:
                attempts -= 1
                print(f"Incorrect password! {attempts} attempts left.")

        print("\nYou have used all attempts.")
        option = input("Do you want to try one last time? (yes/no): ").lower()

        if option == "yes":
            entered_password = input("Enter your Password: ")
            if entered_password == self.password:
                print("\nLogin successful!")
                return
            else:
                print("\nIncorrect password! Proceeding to security questions...")
        
        self.password_recovery()  

    def display_details(self):
        encoded_name = "*" * len(self.name)
        print(f"\nYour Encoded Name is: {encoded_name} – Fresher")
        print(f"Your Department is: {self.department}")
        print(f"Your Password is: {'*' * len(self.password)}")
        print(f"Re-Type your Password: {'*' * len(self.password)}")

    def start(self):
        self.get_user_details()
        self.answer1 = input(f"Set Security Answer 1: {self.security_q1} ")
        self.answer2 = input(f"Set Security Answer 2: {self.security_q2} ")

        self.display_details()
        self.password_verification()

user = PasswordRecovery()
user.start()

