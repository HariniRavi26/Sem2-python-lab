# question 9  
my_dict = {"a": 10, "b": 20, "c": 30} 
total_sum = 0 
for value in my_dict.values():
    total_sum += value  # Add each value to total_sum
    print("The sum of all items in the dictionary is:", total_sum) 
#question 10 
rows = int(input("Enter the number of rows: ")) 
for i in range(1, rows + 1): # Inner loop for columns
    for j in range(i):
        print(i, end=" ")
        print()
