#today's class program-13 Jan
"""arr = [2, 0, 3, 0, 5, 6]
non_zero_ptr = 0
zero_ptr = 0

while zero_ptr < len(arr):
    if arr[zero_ptr] != 0:
        arr[non_zero_ptr], arr[zero_ptr] = arr[zero_ptr], arr[non_zero_ptr]
        non_zero_ptr += 1
    zero_ptr += 1

print("Array after moving zeros to end:", arr)"""

arr = input("Enter the elements of the array separated by space: ")
arr = list(map(int, arr.split()))

new_arr = []
zeros = 0

for num in arr:
    if num != 0:
        new_arr.append(num)
    else:
        zeros += 1

for i in range(zeros):
    new_arr.append(0)

print("Array after moving zeros to end:", new_arr)

arr = input("Enter the elements of the array separated by space: ")
arr = list(map(int, arr.split()))

zeros = [x for x in arr if x == 0]
non_zeros = [x for x in arr if x != 0]

new_arr = zeros + non_zeros

print("Array after moving zeros to front:", new_arr)







