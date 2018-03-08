# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. 
# If the item is a string, concatenate it onto a new string. 
# If it is a number, add it to a running sum. At the end of your program print the string, 
# the number and an analysis of what the list contains. If it contains only one type, 
# print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. 
# What kind of unexpected input could you get?

def typeList (inputGuy):
    sum = 0
    intCount = 0
    sentence = ''
    wordCount = 0
    for count in inputGuy:
        if isinstance(count, int) or isinstance(count, float):
            sum += count
            intCount += 1
        if isinstance(count, str):
            sentence += count
            wordCount += 1
    if intCount > 0 and wordCount > 0:
        print "mixed"
    elif intCount > 0 and wordCount == 0:
        print "The list you entered is of integer type"
    elif wordCount > 0 and intCount == 0:
        print "The list you entered is of string type"
    else: 
        print "this is a corner case"

    print "int count: " , intCount , ". Sum: " , sum , "word count: " , wordCount , " sentence:" , sentence

typeList(['magical','unicorns'])

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"

# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"