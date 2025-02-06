#1.
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def welcome(self):
        pass

    @abstractmethod
    def test_data(self, name):
        pass

    @abstractmethod
    def count_vowels(self, name):
        pass

    @abstractmethod
    def calculate_grade(self, name, mark1, mark2):
        pass

class MyClass(AbstractClass):
    def welcome(self):
        print("Welcome To WTS!\nWe wish you the Best!!")

    def test_data(self, name):
        print(f"Welcome {name}!\nHave a nice day!")

    def count_vowels(self, name):
        vowels = "aeiou"
        name = name.lower()
        vowel_count = {v: name.count(v) for v in vowels if v in name}
        total_vowels = sum(vowel_count.values())
        print(f"Count of Vowels are: {total_vowels}")
        for vowel, count in vowel_count.items():
            print(f"{vowel} : {count}")

    def calculate_grade(self, name, mark1, mark2):
        total_marks = mark1 + mark2
        if total_marks > 95:
            grade = "E"
        elif 80 <= total_marks <= 95:
            grade = "A+"
        elif 75 <= total_marks < 80:
            grade = "A"
        elif 60 <= total_marks < 75:
            grade = "B"
        else:
            grade = "F"
        print(f"Student: {name}\nTotal Marks: {total_marks}\nGrade: {grade}")
if __name__ == "__main__":
    obj = MyClass()
    obj.welcome()
    name = input("Please input a name: ")
    obj.test_data(name)
    obj.count_vowels(name)
    mark1 = int(input("Enter Mark 1: "))
    mark2 = int(input("Enter Mark 2: "))
    obj.calculate_grade(name, mark1, mark2)

#2.
def break_(password):
    result = ""
    for i in password:
        if i.isdigit():  
            break  
        result += i  
    print("Your Output will Break here -", result)
break_("Welcome1face")

def skip_(password):
    result = ""
    for i in password:
        if i.isdigit():  
            continue 
        result += i  
    print("Your Output will continue -", result)
skip_("Welcome1face")
