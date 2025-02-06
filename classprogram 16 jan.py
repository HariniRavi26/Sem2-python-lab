arr = [1, 2, 4, 5]
n = len(arr) + 1 #5
expected_sum = n * (n + 1) // 2 #15
actual_sum = sum(arr) #12
missing_number = expected_sum - actual_sum #3
print("Missing number is:",missing_number)


def find_duplicate(arr):
    nums=set()
    duplicates=set()
    for i in arr:
        if i in nums:
            duplicates.add(i)
        nums.add(i)
    return [i for i in nums if i not in duplicates]
        
        
from array import *
arr=array('i',[])
n=int(input("Enter how many values you need:"))
for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
print(arr)
print(find_duplicate(arr))



def find_sort(arr):
    if arr==sorted(arr):
        return true
    else:
        return sorted(arr)
from array import *
arr=array('i',[])
n=int(input("Enter how many values you need:"))
for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
print(arr)
print(find_sort(arr))
