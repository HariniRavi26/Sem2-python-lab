#Write a recursive function to reverse a string:
def reversestring_(s):
 if len(s)==0:
 return s
 else:
 return s[-1]+reversestring_(s[:-1])
string="Manju"
print(reversestring_(string))
#Check if a string is a palindrome using recursion
def is_palindrome(s):
 if len(s) <= 1: 
 return True
 if s[0] != s[-1]: 
 return False
 return is_palindrome(s[1:-1]) 
string = "madam"
print("Is palindrome:", is_palindrome(string))
#mplement a recursive function to calculate x power n:
def power(x, n):
 if n == 0:
 return 1
 return x * power(x, n - 1)
x = 2
n = 3
print(f"{x} raised to the power {n} is:", power(x, n))
#Write a recursive function to find the sum of digits of a number:
def sum_(n):
 if n==0:
 return 0
 return n%10+sum_(n//10)
number=125
print(sum_(number))
#2D Array - Sum of All Elements
def 2darray_(arr):
 total=0
 for i in arr:
 total+=sum(i)
 return total
array=[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
print(2darray_(array))
#2D Array - Transpose of a Matrix:
def transpose_matrix(matrix):
 rows = len(matrix)
 cols = len(matrix[0])
 transposed = [[0 for _ in range(rows)] for _ in range(cols)]
 
 for i in range(rows):
 for j in range(cols):
 transposed[j][i] = matrix[i][j]
 
 return transposed
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Transpose of the matrix:")
for row in transposed_matrix:
 print(row)
 
