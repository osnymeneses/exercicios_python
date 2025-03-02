## Você está com fome?

texto1 = input('Você esta com fome?\n').lower()

if texto1 == 'sim' or texto1 == 's':
    texto2 = input('Tem comida em casa?\n').lower()
    if texto2 == 's' or texto2 == 'sim':
        print('Prepare uma refeição para você')
    else: 
        print('Vá ao mercado.')
else:
    print('Quando estiver com fome se alimente bem.')