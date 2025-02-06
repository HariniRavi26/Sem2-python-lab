 #1.
class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    def display_customer_details(self):
        print(f"Customer Name : {self.name}  Customer Phone No. : {self.phone_number}")

class Depositor(Customer):
    def __init__(self, name, phone_number, accno, balance):
        super().__init__(name, phone_number)
        self.accno = accno
        self.balance = balance
    
    def display_depositor_details(self):
        self.display_customer_details()
        print(f"Customer A/C No. : {self.accno}  Balance : {self.balance}")

class Borrower(Depositor):
    def __init__(self, name, phone_number, accno, balance, loan_no, loan_amt):
        super().__init__(name, phone_number, accno, balance)
        self.loan_no = loan_no
        self.loan_amt = loan_amt
    
    def display_borrower_details(self):
        self.display_depositor_details()
        print("-" * 70)
        print(f"Loan No : {self.loan_no}\nLoan Amount : {self.loan_amt}")
        print("-" * 70)


def main():
    customers = []
    n = int(input("Enter number of customer details you want to add : "))
    
    for _ in range(n):
        name = input("Enter Customer Name : ")
        phone_number = input("Enter Customer Phone.No : ")
        accno = input("Enter Customer A/C No : ")
        balance = float(input("Enter Balance : "))
        loan_no = input("Enter Loan number : ")
        loan_amt = float(input("Enter Loan Amount : "))
        print("*" * 50)
        
        customer = Borrower(name, phone_number, accno, balance, loan_no, loan_amt)
        customers.append(customer)
    
    print("Details Of customer")
    print("-" * 70)
    for customer in customers:
        customer.display_borrower_details()

if __name__ == "__main__":
    main()


#2.
nums = list(map(int, input("Enter the binary array elements (space-separated): ").split()))
prefix_sum = {0: -1}
length = len(nums)
count = 0
max_length = 0
for i in range(length):
    if nums[i] == 0:
        count -= 1
    else:
        count += 1
    if count in prefix_sum:
        max_length = max(max_length, i - prefix_sum[count])
    else:
        prefix_sum[count] = i
        print("Length of the longest good subarray:", max_length)



