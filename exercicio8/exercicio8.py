## Pegar os valores de duas listas e imprimir a lista Original, os não repetidos e os repetidos

lista_um = ['Manga', 'Goiaba', 'Banana', 'Melancia']
lista_dois = ['Queijo', 'Banana', 'Maçã', 'Uva', 'Manga']
listas = lista_um + lista_dois

valores = []
valores_repetidos = set()

for i in listas:
    if i not in valores:
        valores.append(i)
    else: 
        valores_repetidos.add(i)

print(f'Lista Original {listas}\n')
print(f'Valores não Repetidos: {valores}\n')
print(f'Valore Repetidos: {valores_repetidos}\n')