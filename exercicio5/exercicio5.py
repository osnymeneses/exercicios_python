# Em uma lista de palavras print todas as palavras com pelo menos 5 caracteres.

palavras = ['Cão', 'Banana', 'Melancia', 'Cavalo', 'Gato', 'Papagaio', 'Uva']

for palavra in palavras:
    if len(palavra) <= 5:
        print(palavra)