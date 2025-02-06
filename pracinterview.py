"""arr=list(input().split())
for index,element in enumerate(arr):
    print(f"Element is {element} and it's index - {index}")

arr=list(input("Enter the elements in array:").split())
arr.pop(int(input("Enter the element to be removed:")))
for i in arr:
    print(arr)
    break

arr=list(input("Enter the elements: ").split())
element_remove=int(input("Enter the index of element to be removed: "))
if 0 <= element_remove < len(arr):
    updated_arr=[]
    for i in range(len(arr)):
        if i!=element_remove:
            updated_arr.append(arr[i])
            print(updated_arr)
else:
    print("Element not found")

arr=list(input("Enter the elements to:").split())
element_added=int(input("Enter the index of element to be added:"))
element_to_be_added=input("Enter the element to be inserted:")

arr = list(input("Enter the elements of the array:"))
index_to_insert = int(input("Enter the index of the element:"))  
element_to_insert = int(input("Enter the element to be inserted:"))

new_arr = []

for i in range(len(arr) + 1): #4
    if i == index_to_insert:
        new_arr.append(element_to_insert)
    if i < len(arr):
        new_arr.append(arr[i])

print(f"Original Array: {arr}")
print(f"Updated Array: {new_arr}")

arr=list(input("Enter the elements in array:").split())
for index,element in enumerate(arr):
    print(f"Element is {element} and it's index - {index}")

for index,element in enumerate(arr):
    if index%2==0:
        print(f"Even elements are:")
        print(f"Element is {element} and it's index - {index}")
for index,element in enumerate(arr):
    if index%2!=0:
        print(f"Odd elements are:")
        print(f"Element is {element} and it's index - {index}")


a=int(input())
for i in range(2,a):
    if a%i==0:
        print("Not a prime")
        break
    else:
        print("Its a prime")
        break


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*fact(n-1)) 
a=int(input("Enter a number:"))
print(f"The factorial is {fact(a)}")

#encapsulation
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        if new_name.isalpha():
            self.__name=new_name
        else:
            print("Invalid name !")

    def get_age(self):
        return self.__age
    def set_name(self,new_age):
        if new_age>=0 and new_age <=100:
            self.__age=new_age
        else:
            print("Invalid Age !")


student=Student("Harini",18)

'''print(student.get_name())
print(student.get_age())'''

student.set_name("Harini")
student.set_age(18)


#inheritance
class Vehicle:
    def __init__(self,color,max_speed):
        self.color=color
        self.max_speed=max_speed

class car(Vehicle):
    def __init__(self,color,max_speed,num_doors):
        super().__init__(color,max_speed)
        self.num_doors=num_doors
    def display_details(self):
        print(f"Color of the car : {self.color}")
        print(f"Maximum speed is : {self.max_speed}")
        print(f"Number of doors : {self.num_doors} ")

details=car("Green", "120/km", 4)
details.display_details()

# swap numbers
a=int(input())
b=int(input())
print(f"a: {b} , b: {a} ")

num=int(input("Enter a digit :"))
first=num//100
second=(num//10)%10
third=num%10
final=first+second+third
print(final)

num=int(input())
sum_digits=0
while num > 0:
    sum_digits+=num%10 #4
    num//=10 #1230

print(sum_digits)

#number triangle
num=int(input())
for i in range(num):
    for j in range(i):
        print(i , end=" ")
    print()


#inverted pyramid
num=int(input())
a=0
for i in range(num,0,-1):
    a+=1
    for j in range(1,i+1):
        print(a , end=" ")
    print()

#half pyramid pattern
a=int(input("Enter a number"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#inverted pyramid pattern

a=int(input())
for i in range(a,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()

#reverse pyramid
a=int(input())
for i in range(1,a+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

base=int(input())
height=int(input())
area= 0.5*base*height
print(int(area))

celsius=float(input("Enter celsius :"))
fahrenheit=(celsius*9/5) +32
print(f"Celsius to fahrenheit is {fahrenheit} ")

fahrenheit=float(input("Enter fahrenheit : "))
celsius = (fahrenheit * 5/9) -32
print(f"Fahrenheit to celsius is {celsius}")


import calendar

year=int(input())
month=int(input())
cal = calendar.month(year,month)
print(cal)

year=int(input())
if (year % 400 ==0 ) and (year % 100==0):
    print(f" {year} is a leap year".format(year))
elif (year % 4==0) and (year % 100!=0):
    print(f" {year} is a leap year".format(year))
else:
    print(f" {year} is not a leap year")


#prime number between
lower=1
upper=10
print(f"The prime numbers between {lower} and {upper} are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)
                break
               

#factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return (n * fact(n-1))

num=int(input())
print(fact(num))

#multiplication table
num=int(input())
for i in range(1,11):
    print(num*i)

#vowel consonant
a=input("Enter a string:")
if a.isalpha():
    if a.lower() in "aeiou":
        print("The string is a vowel")
    else:
        print("The string is a consonant")
else:
    print("Invalid input")

#fibonacci
num=int(input())
a,b=0,1
print(a)
print(b)
for i in range(num):
    a,b=b,a+b
    print(b,end=" ")
    print()

nterms=int(input())
a,b=0,1
count=0
while count<nterms:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1

#armstrong number
num=int(input())
num_str=str(num)
num_digits=len(num_str)
sum_powers=0
temp_num=num
while temp_num>0:
    digit=temp_num%10#4
    sum_powers+=digit**num_digits
    temp_num//=10

if sum_powers==num:
    print("Its an armstrong number")
else:
    print("No its not an Armstrong number")

#palindrome
def is_palindrome(string):
    reversed_string=string[::-1]
    if string==reversed_string:
        print("Its a palindrome")
    else:
        print("Its a non palindrome")

s=input()
is_palindrome(s)

#sum of prime numbers
num = int(input("Enter a number: ")) 
sum_of_primes = 0

for n in range(2, num + 1):  
    is_prime = True  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_of_primes += n  

print(f"Sum of prime numbers up to {num}: {sum_of_primes}")

num=int(input())
for i in range(0,num+1):
    for j in range(i):
        print("*",end=" " )
    print()

start=int(input())
end=int(input())
div_four=0
for i in range(start,end+1):
    if i%2==0 and i%4!=0:
        div_four+=i

print(div_four)

char = input("Enter a character: ")
ascii_val = ord(char)

if 65 <= ascii_val <= 90:
    print(f"'{char}' is an Uppercase Letter")
elif 97 <= ascii_val <= 122:
    print(f"'{char}' is a Lowercase Letter")
elif 48 <= ascii_val <= 57:
    print(f"'{char}' is a Digit")
else:
    print(f"'{char}' is a Special Character")


input_string=input("Enter a string")
vowel="AEIOUaeiou"

result=""
for char in input_string:
    if char.isalpha():
        if char in vowel:
            result+="*"
        else:
            result+="."

print(result)

#hollow square:
size=int(input())
for i in range(size):
    for j in range(size):
        if i==0 or i==size-1 or j==0 or j==size-1:
            print("*" ,end=" ")
        else:
            print(' ',end=" ")
    print()

num=int(input())

#reverse a number
num=int(input())
reverse_num=0 #321
while num>0:
    digit=num%10 #3 #2 #1
    reverse_num=reverse_num*10+digit 
    num//=10
print(reverse_num)

input_string=input("Enter a string")
vowel="AEIOUaeiou"

result=""
for char in input_string:
    if char.isalpha():
        if char in vowel:
            result+="1"
        else:
            result+="0"
print(result)

num = int(input("Enter a number: "))
sum_of_odd_non_prime = 0

for i in range(1, num + 1, 2):  # Loop through odd numbers only
    if i > 1:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Check for prime
            if i % j == 0:
                is_prime = False
                break
        if not is_prime:  # If NOT prime, add to sum
            sum_of_odd_non_prime += i
    else:
        sum_of_odd_non_prime += i  

print(f"Sum of odd non-prime numbers: {sum_of_odd_non_prime}")

input_str=input("Enter a string:")
vowel="AEIOUaeiou"
for i in input_str:
    if i in vowel:
        print("0",end=" ")
    else:
        print("1",end=" ")"""















        


