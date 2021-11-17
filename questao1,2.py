c = 0
for c in range (1, 5000001):
    if (c % 2 == 0 and c % 37 == 0 and c % 49 == 0):
        print (c, end=' ')