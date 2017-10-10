n = 8


for i in range(1,n):
    print "*",
    for j in range(1,n/2+1):
        
        if (i == 1 or i == 7) and (j != 4):
            print "*",
        elif (i != 1 and i != 7) and j == 4:
            print "*",
        else:
            print " ",
    print
