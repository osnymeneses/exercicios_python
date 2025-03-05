# Contar o número de vogais no código
# Desconsiderar se a letra é maiuscula ou minusculas
# E Imprimir o resultado

# Solução 1
texto = """
Não é a linguagem de programação que define o programador, mas sim sua lógica.
Faça como um programador. Quando tudo está errado e confuso, apague tudo e recomece do zero.
Programadores e artistas são os únicos profissionais que tem como hobby a própria profissão.
Ser desenvolvedor é uma viagem onde a próxima parada é a solução de um problema.
"""
vogais = ['a', 'e', 'i', 'o', 'u']

for v in vogais:
    print(f'A vogal "{v}" aparece {texto.lower().count(v)} vezes no texto.')


# Solução 2
# texto = """
# Não é a linguagem de programação que define o programador, mas sim sua lógica.
# Faça como um programador. Quando tudo está errado e confuso, apague tudo e recomece do zero.
# Programadores e artistas são os únicos profissionais que tem como hobby a própria profissão.
# Ser desenvolvedor é uma viagem onde a próxima parada é a solução de um problema.
# """

# vogais = {
#     'A': 0,
#     'E': 0,
#     'I': 0,
#     'O': 0,
#     'U': 0,
# }

# for caractere in texto:
#     if caractere.upper() == 'A':
#         vogais['A'] += 1
#     if caractere.upper() == 'E':
#         vogais['E'] += 1
#     if caractere.upper() == 'I':
#         vogais['I'] += 1
#     if caractere.upper() == 'O':
#         vogais['O'] += 1
#     if caractere.upper() == 'U':
#         vogais['U'] += 1

# for vogal, contagem in vogais.items():
#     print(f'Há {contagem} letras {vogal} no texto.')