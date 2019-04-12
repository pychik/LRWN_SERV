string = '1192010000'

fin = 'неизвестный пакет' + str(string)
if string.startswith('11'):
    print('recieved zenner payload sp1')
    a1 = string[8:10]
    a2 = string[6:8]
    a3 = string[4:6]
    a4 = string[2:4]
    a = a1 + a2 + a3 + a4
    fin = int(a,16)
print(fin)
#mes = 'Bearer '
#MES = 'Bearer ' + string
#print(MES)
