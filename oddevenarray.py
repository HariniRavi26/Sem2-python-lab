arr=list(input("Enter the elements of the array:").split())
print(f"Elements at odd position:")
for index,element in enumerate(arr):
    if index%2!=0:
        print(f"Index {index} ,Value {element} ")
        
print(f"Elements at even position:")
for index,element in enumerate(arr):
    if index%2==0:
        print(f"Index {index} , Value {element} ")
