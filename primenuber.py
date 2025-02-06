#primenumber
num=int(input())
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")


#factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input())
print(f"Factorial is {factorial(num)}")

#swap two numbers
n=int(input())
m=int(input())
n,m=m,n
print(n,m)

#sum of numbers
num = int(input("Enter a number: "))#123
sum_of_digits = 0

while num != 0:
    digit = num % 10#32
    sum_of_digits += digit
    num //= 10#12 , 2

print("Sum of digits:", sum_of_digits)

#hollow square
def print_hollow_square():
    size = 4  # Fixed size for the pattern
    
    for row in range(size):
        if row == 0 or row == size - 1:
            print("*  " * size)
        else:
            print("*  " + "   " * (size - 2) + "*")

print_hollow_square()


#fibbonacci
num = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b












