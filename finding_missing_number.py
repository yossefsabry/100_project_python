# -------------------------------------------------
# make program to find missing number in list
# -------------------------------------------------

# def the main function
def findMissingNumbers(n):

    # define the variable that will hold the missing numbers

    # convert the list to set to remove duplicates (repeats) and sort it and make fast access
    numbers = set(n)
    
    length = len(n) # get the length of the list not very important

    output = [] # to append the missing numbers in it

    for i in range(1,n[-1]): # loop through the list from 1 to the last number in the list
        
        if i not in numbers: # if the number is not in the list

            output.append(i) # append it to the output list
        

    return output # return the output list

# test case
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,20]

# call the function and print the result
print("the missing number is: ",findMissingNumbers(numbers))

