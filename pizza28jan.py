class Pizza_size:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def check_budget(self,budget):
        if not isinstance(budget,(int,float)) or budget < 0:
            raise ValueError("Budget cannot be negative!")
        return True

    def calculate_balance(self,budget):
        return budget-self.price

    def suggest_size(self,budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print(f"You can buy {self.name} . Your balance is {self.calculate_balance(budget)}")

            elif budget==self.price:
                print(f"You can buy {self.name} . No balance ")

            else:
                print(f"You cannot afford {self.name}")

        except ValueError as ve:
            print(ve)


small=Pizza_size("Small",75)
medium=Pizza_size("Medium",100)
large=Pizza_size("Large",150)
packets=[small,medium,large]

try:
    budget=float(input("Enter your budget:"))
    for pack in packets:
        pack.suggest_size(budget)

except ValueError:
    print("Values should be in numbers")
