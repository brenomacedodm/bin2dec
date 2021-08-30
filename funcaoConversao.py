#função de conversão
def bin2dec(binario):
    decimal = 0
    for k in range(len(binario), 0):
        decimal += int(binario[k]) * (2**k)
    return decimal
    
