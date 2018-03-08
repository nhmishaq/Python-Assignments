#This is version 2.0 of the same python platform assignments that I worked on in my first attempt.
#The goal is to implement better coding practices and sharpen my command over the language. 

# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the 
# position of the first instance of the word "day". Then create a new string where 
# the word "day" is replaced with the word "month".
def find(sentence, wordToFind, newWord):
    firstInstance = sentence.find(wordToFind)
    newSentence = sentence.replace(wordToFind, newWord)
    print firstInstance, newSentence
find("It's thanksgiving day. It's my birdhday,too!", "day", "month")

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. 
# Your code should work for any list.
def minAndMax(list):
    print min(list)
    print max(list)
minAndMax([2,54,-2,7,12,98])

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
# Now create a new list containing only the first and last values in the original list. 
# Your code should work for any list.

def firstAndLast(list):
    print list[0]
    print list[len(list)-1]
firstAndLast(["hello",2,54,-2,7,12,98,"world"])

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
# Sort your list first. Then, split your list in half. 
# Push the list created from the first half to position 0 of the list created from the second half. 
# The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 
# Stick with it, this one is tough!
def newList(list):
    list.sort()
    list.append(list[len(list)/2])
    print list
newList([19,2,54,-2,7,12,98,32,10,-3,6])