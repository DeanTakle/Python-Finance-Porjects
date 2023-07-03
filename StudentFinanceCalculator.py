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
    salary_after_uni(tuition_fees, maintenance_loan, how_much_maintenance_loan)

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
        pass
    elif what_year_did_you_go_to_uni >= 2013 or what_year_did_you_go_to_uni <= 2022:
        pass
    elif what_year_did_you_go_to_uni >= 2023:
        pass
    else:
        print('Enter a valid year')

# User enters when they finished uni


def what_year_finsihed():
    what_year_did_you_finish_uni = int(input('Enter year of finishing uni?: '))
    if what_year_did_you_finish_uni <= 2012:
        pass
    elif what_year_did_you_finish_uni >= 2013 or what_year_did_you_finish_uni <= 2022:
        pass
    elif what_year_did_you_finish_uni >= 2023:
        pass
    else:
        print('Enter a valid year')

# User enters where they went to uni - England, Scotland, Wales, Northern Ireland


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


def salary_after_uni(tuition_fees, maintenance_loan, how_much_maintenance_loan):
    salary_after_uni_amount = int(input('What is your salary?: '))
