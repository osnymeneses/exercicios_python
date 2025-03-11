# Cifra de César em Python

# Solução 1
# def cifrar_caractere(caractere, sequencia, chave):
#     indice_atual = sequencia.index(caractere)
#     novo_indice = indice_atual + chave
    
#     # Lidar com situação onde o indice está a direita da sequencia
#     while novo_indice >= len(sequencia):
#         novo_indice -= len(sequencia)

#     # Lidar com situação onde o indice está a direita da sequencia
#     while novo_indice < 0:
#         novo_indice += len(sequencia)
#     return sequencia[novo_indice]

# letras_alfa_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# letras_alfa_minusculas = 'abcdefghijklmnopqrstuvwxyz'

# texto = 'olá mundo!'.upper()
# chave = 5

# cifra = ''

# for caractere in texto:
#     if caractere == letras_alfa_minusculas:
#         caractere_cifra = cifrar_caractere(caractere, letras_alfa_minusculas, chave)
#     elif caractere in letras_alfa_maiusculas:
#         caractere_cifra = cifrar_caractere(caractere, letras_alfa_maiusculas, chave)
#     else:
#         caractere_cifra = caractere
#     cifra += caractere_cifra

# print(cifra)



# Solução 2
letras_alfa_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_alfa_minusculas = 'abcdefghijklmnopqrstuvwxyz'

# Conjunto de caracteres válidos no algoritmo
letras = letras_alfa_maiusculas + letras_alfa_minusculas

# Variável para armazenar o texto criptografado (ou decifrado)
convertido = ''

# Solicitar o texto a ser encriptado ou decriptado
criptografar_texto = input('Digite o texto a ser encriptada ou decifrada: ')

# Chave a ser utilizada
chave = int(input('Digite o valor numérico de uma chave: '))

# Conjunto de caracteres válidos no algoritmo
modo = input('Escolha E para encriptar ou D para decriptar o texto: ')

# Código que será executado em cada caractere do texto:
for caractere in criptografar_texto:
    if caractere in letras:
        num = letras.find(caractere)
        if modo == 'E' or modo == 'e':
            num += chave
        elif modo == 'D' or modo =='d':
            num -= chave

        # Manipular a rotação se o valor de num for maior do que o comprimento de CARACTERES ou menor que 0
        if num >= len(letras):
            num -= len(letras)
        elif num < 0:
            num += len(letras)
        # Adicionar (concatenar) o caractere correspondente a num na variável convertido
        convertido += letras[num]
    else:
        # Concatenar o caractere sem efetuar criptografia ou decifragem
        convertido += caractere

# Mostrar o texto encriptado ou decifrado na tela
if modo == 'E' or modo == 'e':
    print('O texto criptografado é ', convertido)
elif modo == 'D' or modo == 'd':
    print('O texto decriptado é ', convertido)
else:
    print('Opção inválida')

    

