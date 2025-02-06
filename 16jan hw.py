Tech Task 16.01.25
#Find the Missing Number:
arr=[1,2,4,5,6,8]
missing=[]
for i in range(arr[0],arr[-1]+1):
    if i not in arr:
        missing.append(i)
        print(missing)
#Find the Duplicates:
arr=[1,2,3,4,3,5,6,7,8,7]
seen=set()
duplicate=[]
for i in arr:
    if i in seen:
        duplicate.append(i)
    else:
        seen.add(i)
        print(duplicate) 
#Check if Array is Sorted:
arr=[1,2,3,4,5]
if arr==sorted(arr):
    print(True)
else:
    print(False)
#Find the Majority Element:
def majorityElement(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                if count > n // 2:
                    return arr[i]
                return -1
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majorityElement(arr))
#Check for Balanced Array:
def isBalancedArray(arr):
 for i in range(len(arr)):
 left_sum = sum(arr[:i]) 
 right_sum = sum(arr[i+1:]) 
 if left_sum == right_sum: 
 return True
 return False 
arr = [1, 2, 3, 4, 10, 1, 2, 3]
print(isBalancedArray(arr)) 
#Find All Pairs in an Array that Sum to a Specific Target:
def find_pairs(arr, target):
 seen = set() 
 pairs = [] 
 
 for num in arr:
 complement = target - num 
 
 if complement in seen:
 pairs.append((complement, num))
 seen.add(num)
 
 return pairs
arr = [2, 4, 3, 5, 7, 8]
target = 10
print(find_pairs(arr, target))

#9.Sum of all items in a dictionary:
dict_={"a":10,"b":20,"c":30}
sum_=sum(dict_.values())
print(sum_)
#10.Construct a pattern using a nested loop
#Pattern: 
#1
#2 2
#3 3 3
#4 4 4 4:
rows=int(input())
for i in range(1,rows+1):
 for j in range(i):
 print(i,end=" ")
 print() 
