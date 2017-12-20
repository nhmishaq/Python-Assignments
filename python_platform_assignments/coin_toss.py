from random import *
def coin_toss():
    tosses = []
    heads = 0
    tails = 0
    for num in range (0, 5000):
        score_list = round(uniform(0, 1))
        tosses.append(score_list)
        if score_list == 1.0:
            heads += 1
            print "you have " + str(heads) + " heads so far"
        elif score_list == 0.0:
            tails += 1
            print "you have " + str(tails) + " tails so far"
    print heads
    print tails
coin_toss()