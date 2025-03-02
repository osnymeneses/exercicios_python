# Em duas listas, print todos os valores que aparecem duplicados nas duas listas.

lista_um = ['Manga', 'Goiaba', 'Banana', 'Melancia']
lista_dois = ['Queijo', 'Banana', 'Maçã', 'Uva', 'Manga']

for l1 in lista_um:
    for l2 in lista_dois:
        if l1 == l2:
            print(f'O valor {l1} aparece nas duas listas.')