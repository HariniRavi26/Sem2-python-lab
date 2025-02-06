"""#convert lowercase to uppercase
character=input()
if 'a'<=character <='z':
    c=ord(character)-32
converted=chr(c)
print(converted)

#convert whole string to lowercase
ch=input()
for i in ch:
    if 'A'<=i<='Z':
        p=ord(i)
        q=chr(p+32)
        print(q,end=" ")

#mixed upper to lower  
def lowcase(ch):
    p=ord(ch)
    q=chr(p+32)
    print(q,end=" ")
def upcase(char):
    x=ord(char)
    y=chr(x-32)
    print(y,end=" ")
string1=input()
for i in string1:
    if 'A'<=i<='Z':
        lowcase(i)
    elif 'a'<=i<='z':
        upcase(i)




#convert upper to lower from list of string
names_input = input("Enter names separated by spaces: ").split()
for name in names_input:
    for char in name:
        if 'A' <= char <= 'Z':
            print(chr(ord(char) + 32), end="")
        else:
            print(char, end="")
    print("", end=" ")

#length without len and reverse without its index 
def reverse_string(s):
    length=0
    reverse=""
    for i in s:
        length+=1
    for i in range(length-1,-1,-1):#(5,-1,-1)
        reverse+=s[i]
    return reverse

string=input("Enter a string:").strip()
rev=reverse_string(string)
print(rev)

#replace the letter in a given string without replace
string=input("Enter a string:").strip()#harini
to_replace=input("Enter a character to replace:")#a
replace_with=input("Enter a character to replace with:")#e

replaced_string=""

for c in string:
    if c==to_replace:
        replaced_string+=replace_with
    else:
        replaced_string+=c
print(replaced_string)

#sum of only prime numbers
numbers=list(map(int,input("Enter a number by space separated:").split()))
total=0

for n in numbers:
    if n<2:
        f=False
    else:
        f=True
        for i in range(2,n):
            if n%i==0:
                f=False
                break
        if f:
            total+=n
print("Sum of prime numbers is:",total)"""

def is_prime(p):
    if p<2:
        return False
    if p==2:
        return True
    for i in range(2,p):
        if p%i==0:
            return False
    return True

def sum_digits(s):
    total=0
    for i in str(s):
        if is_prime(int(i)):
            total+=int(i)
    return total


n=int(input())
result=sum_digits(n)
print(result)


        




