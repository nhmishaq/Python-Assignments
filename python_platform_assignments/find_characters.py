def find_characters(my_list, char_check):
    new_list = []
    for num in my_list:
        if (num.find(char_check) > 0):
            new_list.append(num)
    print new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
find_characters (word_list, char)