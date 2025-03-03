# Verificar se em duas listas existem elementos em comum.

lista_um = [10.5, True, 2, 'xx']
lista_dois = ['xxx', False, 2, 10]

elementos_em_comum = False

for l1 in lista_um:
    if elementos_em_comum:
        break
    for l2 in lista_dois:
        if l1 == l2:
            elementos_em_comum = True
            break
    
if elementos_em_comum:
    print(f'As listas {lista_um} e {lista_dois} possuem elementos em comum.')
else:
    print(f'As listas {lista_um} e {lista_dois} não possuem elementos em comum.')
            