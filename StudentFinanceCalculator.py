# User enters period of time at uni
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

# User enters where they went to uni - England, Scotland, Wales, Northern Ireland

# User enters how much they a year they pay in tuition fees - max 9250

# User enters if they took a maintance loan

# User enters how much they get in maintenance loan

# User enters salary - if 2012 >= 25000, after 2012 >= 27000, after 2023 >= 25000
