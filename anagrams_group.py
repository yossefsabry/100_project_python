# first import defaultdict from collections
from collections import defaultdict


# second define a function that takes in a list of strings
def group_anagrams(strs):

    # create a default dict that takes in a list
    anagrams = defaultdict(list)

    # loop through the list of strings
    for i in strs:

        # sort the strings and join them
        # use the sorted string as the key and append the original string to the list
        anagrams[''.join(sorted(i))].append(i)

    # return the values of the dictionary
    # why see values instead of keys?
    # because the values are the original strings
    # the keys are the sorted strings
    #  if keys he will add only one key and the values will be the original strings
    return list(anagrams.values())

# test case
words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab","cat","act"]

# call the function and print the result
print(group_anagrams(words))