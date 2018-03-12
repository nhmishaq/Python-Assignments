def findChars2 (inputList, inputChar):
    wordsThatContainChar = []
    for count in inputList:
        if (count.find(inputChar) > 0):
            wordsThatContainChar.append(count)
    print wordsThatContainChar

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChars2 (word_list, char)