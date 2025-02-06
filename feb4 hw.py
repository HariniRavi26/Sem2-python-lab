
#1
s = input("Enter a string: ").strip()
words = s.split()
last_word = words[-1]
print(len(last_word))
#2
def add_binary():
    a = input("Enter first binary string: ")
    b = input("Enter second binary string: ")
    num1 = int(a, 2)
    num2 = int(b, 2)
    sum_num = num1 + num2
    binary_sum = bin(sum_num)
    print("Sum of binary strings:", binary_sum)
add_binary()
