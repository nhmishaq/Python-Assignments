def type_list(my_list):
    sum = 0
    num_count = 0
    str_count = 0
    ongoing_string = ''
    for num in my_list:
        if (type(num) is int):
            sum += num
            num_count += 1
        elif (type(num) is str):
            ongoing_string += num
            str_count += 1
    if (num_count>0 and str_count>0):
        print "you have a mixed list"
    if (num_count>0 and str_count==0):
        print "you have list of integers"
    if (num_count == 0 and str_count>0):
        print "you have a list of strings"
    print num_count
    print str_count
    print sum
    print ongoing_string

type_list(['magical','unicorns'])
