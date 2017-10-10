


n = 5

for i in range(1,n+1):
    for j in range(1,n+1):
        if (j == 2 or j == 3 or j == 4) and i == 1:
            print " ",
        elif j == 3 and i == 2:
            print " ",
        elif (j == 2 or j == 4) and i == 3:
            print " ",
        elif (j == 2 or j == 3 or j == 4) and (i == 4 or i == 5):
            print " ",
        else:
            print "*",
    print

