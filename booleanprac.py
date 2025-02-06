x=1
print(bool(x))
x=0
print(bool(x))
x=-8
print(bool(x))


my_dict={"student_name":"harini" ,"phone number":75673890,"student_name":"elakiya","phone number":639237}
print(my_dict)

def guess_number():
    print("Think between 100 and 999")
    lower_=100
    upper_=999
    while True:
        guess=(lower_+upper_)//2
        print(f"\n my guess is : {guess}")
        feedback=input("Is my guess correct?(Type 'yes' if correct, 'before' if your number is befor my guess , or 'after' if it's after my guess):")
        if feedback=='yes':
            print(f"I guessed the number correctly {guess}")
            break
        elif feedback=='before':
            upper_=guess-1
        elif feedback=='after':
            lower_=guess+1
        else:
            print("Invalid input!")

guess_number()
        
