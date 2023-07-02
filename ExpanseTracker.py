from Expense import Expense


def main():
    print(f'Welcomme to Expense Tracker')
    expense_file_path = 'expenses.csv'
    budget = int(input('Enter your budget for this month: '))
    expenses = get_user_expense()
    save_expense_to_file(expenses, expense_file_path)  # Save to file
    summarize_expenses(expense_file_path, budget)  # Read file and summarize expenses


def get_user_expense():
    print(f'Getting User Expense')
    expense_name = input('Enter Expense Name: ')
    # used to convert amount into float as money is in decimal
    expense_amount = float(input('Enter Expense Amount: '))
    # used format string to print the value of variable inside the string

    expense_category = [
        'Food',
        'Clothing',
        'Transportation',
        'Bills',
        'Miscellaneous',
    ]

    while True:
        print('Select a category for your expense: ')
        # used to get a list of tuples with each index and value of expense_category
        for i, category_name in enumerate(expense_category):
            # i+1 is used to start the index from 1 instead of 0
            print(f'  {i + 1}. {category_name}')

        # used to print the range of values the user can select
        value_length = f' [1 - {len(expense_category)}]'
        selected_index = int(
            input(f'Enter a category number {value_length}: ')) - 1

        if i in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print('Invalid Option, Try Again')


def save_expense_to_file(expenses: Expense, expense_file_path):
    print(f'Saving User Expense to File: {expenses} to {expense_file_path}')
    # used to append the file if it exists, f is the file object
    with open(expense_file_path, 'a') as f:
        # used to write the expense to the file. CSV means Comma Separated Values = {},{},{}\n
        f.write(f'{expenses.name}, {expenses.amount}, {expenses.category}\n')


def summarize_expenses(expense_file_path, budget):
    print(f'Summarizing Expenses of File: {expense_file_path}')
    # used to tell python that this variable is a list of Expense objects
    expenses: list[Expense] = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expenses_name, expenses_amount, expenses_category = line.strip().split(
                ',')  # used to split the line and strip the whitespace
            line_expense = Expense(
                name=expenses_name, amount=(
                    expenses_amount), category=expenses_category
            )
            # used to append the line_expense to the expenses list
            expenses.append(line_expense)

    amount_by_category = {}
    # does not know what this is, will have to change expesnes to expenses: list[Expense] to define that this refers to the list within expesnes
    for expense in expenses:
        keys = expense.category
        if keys in amount_by_category:
            amount_by_category[keys] += expense.amount
        else:
            amount_by_category[keys] = expense.amount

    print('Total Expenses by Category')
    # used to get the key and value of the dictionary, makes pritning look nicer
    for key, amount in amount_by_category.items():
        print(f' {key}: £{amount:.2f}')

    # sum takes a list as an argument, list comprehension is used to get just the amount of each expense in the list
    total_expenses = sum([expense.amount for expense in expenses])
    print(f'Total Expenses: £{total_expenses:.2f} this month')

    remaining_budget = budget - total_expenses
    if remaining_budget > 0:
        print(f'You are £{remaining_budget:.2f} under budget')
    elif remaining_budget < 0:
        print(f'You are £{-remaining_budget:.2f} over budget2')


if __name__ == "__main__":  # If this file is run directly, run main()
    main()
