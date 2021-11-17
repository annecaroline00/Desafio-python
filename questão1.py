#c = 0
#for c in range (1, 50000001):
#    if (c % 2 == 0 and c % 37 == 0 and c % 49 == 0 ):
#        print (c, end='')



cont = 0
for num in range (1, 50000001):
    if num % 2 == 0:
        if num % 37 == 0:
            if num % 49 == 0:
                cont += num


print ('quantidade:' , cont)





