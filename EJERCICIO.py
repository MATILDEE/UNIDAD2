author = 'Matilde Diaz Garcia'

numeros =edges =[6,8,9,12,23,9,65,33]
"""n = len (numeros)
for x in range (1, n + 1):
     print (numeros.index(x)-1,x)"""
print (numeros)

x = numeros[-2]
numeros[-2] = numeros [1]
numeros [1] = x
print (numeros)

# print (numeros [:: -1])

