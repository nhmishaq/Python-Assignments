def type_checker(value):
    if (type(value) is int):
        if (value >= 100):
            print "wow that's a large number"
        else:
            print "that's a small number"
    elif (type(value) is str):
        if ((len(value))>=50):
            print "long sentence"
        else:
            print "short sentence"
    elif (type (value) is list):
        if (len(value)>=10):
            print "Big List"
        else:
            print "Short List"
type_checker([4,34,22,68,9,13,3,5,7,9,2,12,45,923])