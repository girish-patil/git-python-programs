




n = 8


for i in range(1,n):
    for j in range(1,n/2+2):

        if (j == 2 or j == 3 or j == 4) and (i == 1 or i == 7):
            print "*",
        elif (i == 2 or i == 3 or i == 4 or i == 5 or i == 6) and j == 1:
            print "*",
        elif (i == 2 or i == 4 or i == 5 or i == 6) and j == 5:
            print "*",
        elif i == 4 and (j == 3 or j == 4):
            print "*",
        else:
            print " ",
    print
