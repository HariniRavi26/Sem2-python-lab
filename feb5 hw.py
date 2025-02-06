#1.
def longest_common_prefix(strs):
    prefix=strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix
n=int(input("Enter the number of strings: "))
strs=[input(f'Enter a string: ')for i in range(n)]
print("Longest Common prefix: ",longest_common_prefix(strs))

#2.
def is_subsequence(s, t):
    if not s:
        return True
    s_index = 0
    for char in t:
        if char == s[s_index]:
            s_index += 1
            if s_index == len(s):
                return True
    return False 

s = input("Enter the subsequence string: ")
t = input("Enter the main string: ")

print(is_subsequence(s, t))

