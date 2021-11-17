i = 1
dic = {}

while (i <=5):
    try:
        print('aluno', i)
        nota = float(input('digite a nota: '))
        print('-#-#-#-#-#-#-#-#-')

        dic['aluno' + str(i)] = nota

        i += 1
    
    except:
        print('navi não aceitou esse embarque. tente novamente. \n')

print ('o felizardo da maior nota é ', max(dic, key=dic.get), 'com nota igual a', dic[max(dic, key=dic.get)])
