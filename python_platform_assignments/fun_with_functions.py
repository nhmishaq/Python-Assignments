# def odd_even():
#     for value in range (1000, 2000):
#         if value % 2 == 0:
#             print str(value) + " even"
#         else:
#             print str(value) + " odd"

# odd_even()

def multiply(list_given, multiplier):
    for value in list_given:
        # print value
        # print list_given
        b = value * multiplier
        print b

a = [2,4,6,8,10]
by = 5
multiply (a, by)
