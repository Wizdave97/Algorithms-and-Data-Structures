import math
def is_leap_year(year):
    if year%4 !=0:
        return False
    elif year%100 !=0:
        return True
    elif year%400 !=0:
        return False
    else:
        return True
def days_between_dates(birth_date,current_date):
    """Calculates the age in days based on the values provided
        Args:
            arg1: string containg the birth date in the form '10,June,1994'
            arg2: string containing the current date in the form '10,June,2019'
        return value: a string describing the age in days
     """
    try:
        birthday,birth_month,birth_year=birth_date.split(',')
        birthday=int(birthday)
        birth_month=birth_month.title()
        birth_year=int(birth_year)
        current_day,current_month,current_year=current_date.split(',')
        current_day=int(current_day)
        current_month=current_month.title()
        current_year=int(current_year)
        if birth_year>current_year:
            raise
        months=['January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October','November', 'December']
        days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        is_leap=is_leap_year(birth_year)
        birth_month_index=months.index(birth_month)
        current_month_index=months.index(current_month)
        #To calculate days lived in years inbetween the birth year and the current year
        if birth_year==current_year:
            days_lived_inbetween=0
        else:
            days_lived_inbetween=0
            for year in range(birth_year+1,current_year):
                if(is_leap_year(year)):
                    days_lived_inbetween+=366
                else:
                    days_lived_inbetween+=365
        #To calculate days lived in the year of birth
        days_passed_before_birth=0
        for i in range(birth_month_index):
            days_passed_before_birth+=days_in_month[i]
        if(is_leap):
            days_lived_in_birth_year=366-(days_passed_before_birth+birthday)
        else:
            days_lived_in_birth_year=365-(days_passed_before_birth+birthday)
        #To calculate days lived in current year up to the present day
        days_lived_in_current_year=0
        for i in range(current_month_index):
            days_lived_in_current_year+=days_in_month[i]
        if (is_leap_year(current_year)) and current_month_index>2:
            days_lived_in_current_year=days_lived_in_current_year+current_day+1
        else:
            days_lived_in_current_year=days_lived_in_current_year+current_day
        #To calculate total age in days
        if birth_year==current_year:
            age=abs(days_lived_in_current_year-(days_passed_before_birth+birthday))
        else:
            age=days_lived_inbetween+days_lived_in_birth_year+days_lived_in_current_year
        string='You have lived for {} day(s). Congratulations!'.format(age)
        return age
    except Exception as e:
        print('\n {}:please use the prescribed input format'.format(e))
def test():

    test_cases=[(('30,september,2012','30,october,2012'),31),
                (('1,january,2012','1,january,2013'),366),
                (('1,september,2012','4,september,2012'),4),
                (('1,january,2013','31,december,1999'),"AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = days_between_dates(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))


test()
#print(days_between_dates('1,january,2012','1,january,2013'))
