"""class Library:
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is : {book_name} by {user}"

class DigitalLibrary:
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is : {book_name} by {user}"

lib=Library()
dig=DigitalLibrary()

book=input()
username=input()

print(lib.issue_book(book,username))
print(lib.returned_book(book,username))

print(dig.issue_book(book,username))
print(dig.returned_book(book,username))"""


class Book:
    def __init__(self,pages):
        self.pages=pages

        #overloading+operator with magic method
    def __add__(self,other):
        return self.pages+other.pages

b1=Book(400)
b2=Book(300)

print("Total number of pages:",b1 + b2)

class Addition:
    def add(self,a,b,c=0)
    result=0
    result=a+b+c
    return result

a=Addition()
ans=ad.add(2,3)
print(ans)
ans1=ad.add(1,2,3)
print(ans1)

