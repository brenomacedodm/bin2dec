from funcaoConversao import *

#entrada do usuário
binario = str(input())

#funçáo para conferir se os caracteres são 0's e 1's.
var_conf = 0 

for k in range(len(binario)): 
    if (int(binario[k]) == 0 or int(binario[k]) == 1):
        var_conf += 1
    else: 
        var_conf = 0
        break

#chamada da função de conversão
decimal = 0
if (var_conf != 0):
    decimal = bin2dec(binario)
    print("Seu número em decimal é: ", decimal)
