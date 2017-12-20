from random import *

def scores():
    grades = []
    for num in range (0, 10):
        score_list = [uniform(1, 100)]
        grades.append(score_list)
    print grades
    for num in grades:
        print num
        if num >= 60 and num <= 69:
            print str(num) + "Your grade is a D"
        elif num >= 70 and num <= 79:
            print str(num) + "Your grade is a C"
        elif num >= 80 and num <= 89:
            print str(num) + "Your grade is a B"
        elif num >= 90 and num <= 100:
            print str(num) + "Your grade is a A"
        else:
            print "man it's all good dude"
scores()
