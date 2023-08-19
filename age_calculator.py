#---------------------------------
# make app for calculator the age: 
# --------------------------------

# make the main function for the age calculator
def ageCalculator(y, m ,d):

    # import datetime module
    import datetime

    today = datetime.datetime.now().date()

    dateUser = datetime.date(y, m, d)

    # calculate the age

    ageYear = abs(today.year - dateUser.year) 
    ageMonth = abs(today.month - dateUser.month) 
    ageDaY = abs(today.day - dateUser.day)
    return "Your age is: {} years, {} months, {} Days. ".format(ageYear, ageMonth, ageDaY)

# call the calculator function
personOne = ageCalculator(1998, 5, 12)
personTwo = ageCalculator(2009, 3, 22)

print(personOne)
print(personTwo)