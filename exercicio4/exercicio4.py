# Somar todos os numeros de uma sequencia e calcular a media deles, sem usar a função sum()
## Sem a função sum()
total = 0
numeros = [2, 8, 6, 7, 3, 10, 22, 4]
for valor in numeros:
    total += + valor

media = total / len(numeros)
resultado = f'O soma total dos números {numeros} é: {total}. A média dos números é: {media}.'
print(resultado)

### Com a função Sum()
# soma = sum(numeros)
# print(soma)