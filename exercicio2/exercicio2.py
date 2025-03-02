# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeiro_bimestre = float(input('Digite a nota do 1° Bimestre: '))
segundo_bimestre = float(input('Digite a nota do 2° Bimestre: '))
terceiro_bimestre = float(input('Digite a nota do 3° Bimestre: '))
quarto_bimestre = float(input('Digite a nota do 4° Bimestre: '))

media = (primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4
print(f'A média é: {round(media, 1)}.')