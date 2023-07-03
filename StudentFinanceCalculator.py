# User enters period of time at uni
def main():
    print('Welcome to the Student Finance Calculator !UK Edition! ')
    time_at_uni()
    placement()
    what_year_attended()
    what_year_finsihed()
    where_did_you_go_to_uni()
    tuition_fees()
    maintenance_loan()
    how_much_maintenance_loan()
    salary_after_uni(what_year_attended)

# Users eneter how long they spent at uni - 1, 2, 3, 4 years


def time_at_uni():
    time_spent_at_uni = int(input('How many years was your uni degree: '))
    if time_spent_at_uni == 1:
        return 1
    elif time_spent_at_uni == 2:
        return 2
    elif time_spent_at_uni == 3:
        return 3
    elif time_spent_at_uni == 4:
        return 4

# User enters if they went on a placement year


def placement():
    did_you_do_a_placement = input('Did you do a placement year?: ')
    if did_you_do_a_placement == 'yes':
        return 'yes'
    else:
        return 'no'

# User enters when they started uni - before or after 2012 or after 2023 - This will also work out how long they have to pay back their loan - add time section so then only current years can be used


def what_year_attended():
    what_year_did_you_go_to_uni = int(input('Enter year of going to uni?: '))
    if what_year_did_you_go_to_uni <= 2012:
        return what_year_did_you_go_to_uni
    elif what_year_did_you_go_to_uni >= 2013 or what_year_did_you_go_to_uni <= 2022:
        return what_year_did_you_go_to_uni
    elif what_year_did_you_go_to_uni >= 2023:
        return what_year_did_you_go_to_uni
    else:
        print('Enter a valid year')

# User enters when they finished uni


def what_year_finsihed():
    what_year_did_you_finish_uni = int(input('Enter year of finishing uni?: '))
    if what_year_did_you_finish_uni <= 2012:
        return what_year_did_you_finish_uni
    elif what_year_did_you_finish_uni >= 2013 or what_year_did_you_finish_uni <= 2022:
        return what_year_did_you_finish_uni
    elif what_year_did_you_finish_uni >= 2023:
        return what_year_did_you_finish_uni
    else:
        print('Enter a valid year')

# User enters where they went to uni - England, Scotland, Wales, Northern Ireland


def month_finished_uni():  # gets month of finishing uni
    print('Enter month of finishing uni: ')
    return input('Enter month of finishing uni: ')


def where_did_you_go_to_uni():
    where_did_you_go_to_uni = input('Where did you go to uni?: ')
    if where_did_you_go_to_uni == 'England':
        return 'England'
    elif where_did_you_go_to_uni == 'Scotland':
        return 'Scotland'
    elif where_did_you_go_to_uni == 'Wales':
        return 'Wales'
    elif where_did_you_go_to_uni == 'Northern Ireland':
        return 'Northern Ireland'
    else:
        print('Enter a valid country')

# User enters how much they a year they pay in tuition fees - max 9250


def tuition_fees():
    tuition_fees = int(input('How much do you pay in tuition fees?: '))
    if tuition_fees <= 9250:
        return tuition_fees
    else:
        print('Enter a valid amount')

# User enters if they took a maintance loan


def maintenance_loan():
    maintenance_loan = input('Did you take a maintenance loan?: ')
    if maintenance_loan == 'yes':
        return 'yes'
    else:
        return 'no'

# User enters how much they get in maintenance loan


def how_much_maintenance_loan():
    how_much_maintenance_loan = int(
        input('How much do you get in maintenance loan?: '))
    if how_much_maintenance_loan <= 13250:
        return how_much_maintenance_loan
    else:
        print('Enter a valid amount')

# User enters salary - if 2012 >= 25000, after 2012 >= 27000, after 2023 >= 25000


def salary_after_uni(what_year_attended):
    salary_after_uni_amount = int(input('What is your salary?: '))
    if what_year_attended <= 2012:
        if salary_after_uni_amount >= 22015:
            # takes inputted salary and takes away 25k then times by 9% to get amount paid towards loan
            print(
                f'You pay {(salary_after_uni_amount - 22015) / 100 * 9} a year towards your loan')
        else:
            print('YOU PAY £0 TOWARRDS YOUR LOAN')
    elif what_year_attended >= 2013 or what_year_attended <= 2022:
        if salary_after_uni_amount >= 27295:
            # takes inputted salary and takes away 27k then times by 9% to get amount paid towards loan
            print(
                f'You pay {(salary_after_uni_amount - 27295) / 100 * 9} a year towards your loan')
        else:
            print('YOU PAY £0 TOWARRDS YOUR LOAN')
    elif what_year_attended >= 2023:
        if salary_after_uni_amount >= 25000:
            # takes inputted salary and takes away 25k then times by 9% to get amount paid towards loan
            print(
                f'You pay {(salary_after_uni_amount - 25000) / 100 * 9} a year towards your loan')
        else:
            print('YOU PAY £0 TOWARRDS YOUR LOAN')


def total_debt():
    total_debt = tuition_fees + how_much_maintenance_loan
    return total_debt


def how_long_do_you_have():
    if what_year_attended <= 2012 and month_finished_uni == ('September', 'October', 'November', 'December'):
        print('You have 25 years to pay back your loan or its wiped')
    elif what_year_attended <= 2012 and month_finished_uni == ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'):
        print('You have till 65 to pay back your loan or its wiped')
    elif what_year_attended >= 2013 or what_year_attended <= 2022:
        print('You have 30 years to pay back your loan or its wiped')
    elif what_year_attended >= 2023:
        print('You have 30 years to pay back your loan or its wiped')
    return how_long_do_you_have


if __name__ == "__main__":  # If this file is run directly, run main()
    main()
