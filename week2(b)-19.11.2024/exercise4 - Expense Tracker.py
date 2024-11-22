"""
Expense Management Program
--------------------------
This program help to manage personal expenses by categorizing them and calculating totals or averages for predefined categories.
Features to Use:
 •Dictionary with predefined categories as keys, and the values as lists that store expenses.
 •Functions for:
 • Adding expenses to categories
 • Calculating total expenses for a specific category
 • Calculating total and average expenses for all categories
 •Input validation to ensure correct
"""

class ExpenseManage:
    def __init__(self):
        self.expenses = []                              #to store the category and amount of each expense
        self.categories = ["food", "utilities", "entertainment", "transportation", "healthcare"]

    def add_expense(self,category, amount):             #adds an expense.
        if category not in self.categories:
            print(f"Invalid category! Please choose from the predefined categories: {', '.join(self.categories)}")
            return
        try:
            amount = float(amount)                      #converting amounts to floating point mumbers
            self.expenses.append({'category': category, 'amount': amount})
            print(f"Category: {self.expenses[-1]['category']}, Amount: {self.expenses[-1]['amount']}")
                                                        #print the latest expense record
        except ValueError:
            print("invalid amount, please enter again")
                                                        #Exception handling for invalid inputs (e.g., non-numeric expense amounts)


    def get_total_expense_ofonecat(self,category):      #calculates and prints the total expenditures for the category entered.
        if category not in self.categories:
            print(f"Invalid category! Please choose from the predefined categories: {', '.join(self.categories)}")
            return 0

        total_expense_ofonecat = sum(item['amount'] for item in self.expenses if item['category'] == category)
                                                        # Calculate total expense for specified categories using list derivatives
        if total_expense_ofonecat > 0 :
            print(f"Total expense for category '{category}': {total_expense_ofonecat:.2f}")
            return total_expense_ofonecat
        else:
            print(f"Category '{category}' dosen't exist, please enter the right category")
            return 0


    def get_average_expense(self):                      #calculate and print the average expense for every category.
        category_data = {category: {'total': 0, 'count': 0} for category in self.categories}
                                                        #to store totals and counts for each category
        for item in self.expenses:                      #totals and counts by category
            category = item['category']
            amount = item['amount']
            if category not in category_data:           #initialize the category if the category has not yet been recorded
                category_data[category] = {'total': 0, 'count': 0}
            category_data[category]['total'] += amount
            category_data[category]['count'] += 1

        print("Average expense per category:")

        for category, data in category_data.items():
            if data['count'] > 0:
                average = data['total'] / data['count']     #calculate the average
                print(f"{category}: {average:.2f}")
            else:
                print(f"{category}: No expenses recorded.")

def main():
    expensemanage = ExpenseManage()         #reate an instance
    while True:
        command = input("enter command ADD, TOTAL, AVERAGE or EXIT").strip().upper()
        if command == 'EXIT':               # when input exit, stop the book management
            break

        elif command == 'ADD':              # add operation
            category_input = input("please input the name of category: ").lower()
            amount_input = input("please input the amount of expense: ")
            expensemanage.add_expense(category_input, amount_input)

        elif command == 'TOTAL':            # remove operation
            category_input = input("please input the name of category: ").lower()
            expensemanage.get_total_expense_ofonecat(category_input)

        elif command == 'AVERAGE':          # search operation
            expensemanage.get_average_expense()

        else:                               # if the command entered is invalid, direct the user to enter it correctly
            print("invalid command, please enter ADD, TOTAL, AVERAGE or EXIT")


main()