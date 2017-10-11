



n = 8


for i in range(1,n):
    print "*",
    for j in range(1,n/2+1):
        
        if i == 1 or i == 7:
            print "*",
        elif i == 4 and (j == 1 or j == 2 or j == 3):
            print "*",
        else:
            print " ",
    print
