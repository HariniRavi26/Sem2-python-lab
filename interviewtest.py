'''a=input("Enter Your Name:")
print(a.upper())

a=input("Enter your name:")
for i in a:
   if i.isalnum():
       print(i,end=" ")

a=input("Enter your name:")
count=0
for i in a:
    if i.isdigit():
        count+=1
print(f"Your name is - {a} ,Total Number in input is-{count}")'''
    
class Number:
    def __init__(self,name):
        self.name=name
    def get_input(self,name):
        print('enter ur name:',self.name)
    def count_digit(self):
        count=0
        for char in self.name:
            if char.isdigit():
                count+=1
        print(f"Count of digit is - {count}",end=" ")
obj=Number('faceprep123')
obj.count_digit()
