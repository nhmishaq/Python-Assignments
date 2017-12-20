# def checkerboard():
#     for i in range (0, 5):
#         if (i  % 2 != 0):
#             print 5* ' * '
#         else:
#             print ' ' + 5* " * "
# checkerboard()

def checkerStars (num1, num2):
    for i in range (num1, num2):
        if (i % 2 != 0):
            print num2* " * "
        else:
            print " " + num2*" * "

checkerStars (3, 27)