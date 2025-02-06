#1.
n = int(input())#5
for i in range(1,n+1): #
    num = i
    diff = n - 1#4
    for j in range(i):
        print(num,end=" ")
        num+= diff
        diff-= 1
    print()

#2.
arr = [2,1,2,2,2,3,2,1]
arr.sort()
for i in range (len(arr)):
    a=len(arr)//2
    print(arr[a])
    break

#3.
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def topper_mark(self):
        total_marks = sum(self.marks.values())
        average = total_marks / len(self.marks)
        return average


stu1 = Student("Harini", 123, {"tamil": 98, "english": 90})
stu2 = Student("Jeba", 345, {"tamil": 89, "english": 92})
stu3 = Student("Bhuvi", 567, {"tamil": 100, "english": 90})
lists = [stu1, stu2, stu3]


topper = stu1

for student in lists:
    if student.topper_mark() > topper.topper_mark():
        topper = student

print(f"Topper: {topper.name}, Roll No: {topper.rollno}, Average Marks: {topper.topper_mark():.2f}")


#4.
def product_info(name, brand, price, discount=None):
    print(f"name: {name}")
    print(f"brand: {brand}")
    print(f"price: {price}")

    if discount is not None:  # Check if discount is provided
        print(f"discount: {discount}%")
        final_price = price - (price * discount / 100)
        print(f"Final price after discount: {int(final_price)}")  # Convert to int for clean output
    else:
        print("No discount available")

# Sample Input
product_info("Laptop", "Dell", 80000, 10)

n=int(input("Enter:"))#5
for i in range(1,n+1):#1##2#3
    num=i#1`#5#2#6#9#3#7#10
    for j in range(i):#1(0)#2(0,1)#(0,1,2)
        print(num,end=" ")#1#2#6#3#7#10
        num+=(n-j-1)#5#6#9#7#10
    print()
input_lis=input()
arr=list(map(int , input_lis.split()))
x=len(arr)
s=set()
x=x/2#2
for i in arr:#1#2#3
    if arr.count(i)>x:
        s.add(i)
print(s)
        
        
