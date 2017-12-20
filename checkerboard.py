def checkerboard():
    for i in range (8):
        for j in range (8):
            if (i % 2 == 0):
                print '*',
            elif (j % 2 == 0):
                print ' '
    print " ",
checkerboard()