## E uma sequencia de números calcule o mair valor sem usar a função max()

## Sem a função max()
numeros = [10, 5, 9, 10.5, 6, 3, 11, 11.5]
maior_valor = numeros[0]

for numero in numeros:
    if numero > maior_valor:
        maior_valor = numero
print(f'O maior valor entre os números {numeros} é: "{maior_valor}"')

## Com a função max()
# maximo = max(numeros)
# print(maximo)