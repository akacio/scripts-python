def bin_to_str(binario):
    binario = str(binario)
    caractere = ''
    string = ''
    tamanho = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  # 0x101100110
        k += 1
    return string


def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

text = raw_input("Entre com um texto: ")
binary = str_to_bin(text)
print(binary)


binary = raw_input("Entre com um binario: ")
text = bin_to_str(binary)
print(text)
