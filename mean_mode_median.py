# ------------------------------------
# mean mode median => python program
# ------------------------------------

# first mean 

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# the equation for mean is: sum of all numbers / number of items in the list(len)

mean = sum(list_1) / len(list_1)

print("The mean of the list is:",mean)


# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# the median 

list_2 = [ 20, 19, 30, 22, 14,18, 11, 13]

# the equation for median is: middle number of the list
# if the list is even, then the median is the average of the two middle numbers

# first sort the List
list_2.sort()

if len(list_2) % 2 == 0:
    
    item_1 = list_2[len(list_2) // 2]
    item_2 = list_2[len(list_2) // 2 -1]

    median = (item_1 + item_2) / 2

    print("The median of the list is:",median)

if len(list_2) % 2 != 0:
    
    median = len(list_2) // 2

    print("The median of the list is:",median)

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# the mode 

list_3 = [ 20, 19, 30, 22, 14,19, 14, 14]

# the equation for mode is: the number that appears the most in the list

# first sort the List
list_3.sort()

# make dictionary for store the item 
frequency = {}

# loop through the list
for i in list_3:
    # setdefault() method returns the numbers of times a specified value occurs in a string
    frequency.setdefault(i, 0)
    frequency[i] += 1

# print(frequency) => {14: 3, 19: 2, 20: 1, 22: 1, 30: 1} for explantion 

# find the max value in the dictionary
# key = frequency.get => get the value of the key see the height value for the key in dictionary
frequency = max(frequency, key=frequency.get)

print("The mode of the list is:",frequency)

# ------------------------------------
# Path: mean_mode_median.py
# ------------------------------------
# mean mode median => python program
# ------------------------------------


