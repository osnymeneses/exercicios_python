
capitais = {
    'Rio de Janeiro': 'Rio de Janeiro',
    'Acre': 'Rio Branco',
    'Bahia': 'Salvador',
    'Alagoas': 'Maceió',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Maranhão': 'São luis',
    'Piauí': 'Teresina',
    'Amazonas': 'Manaus',
    'Distrito Federal': 'Brasília',
    'Amapá': 'Macapá',
    'Goiás': 'Goiânia',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

quer_continuar = True

for estado, capital in capitais.items():
    if not quer_continuar:
        break

    print(f'Qual é a capital de {estado}?')
    resposta = input('Responda aqui... ')
    
    if resposta.lower() == capital.lower():
        print('Você acertou')
    else:
        print(f'Você errou. A resposta certa é: {capital}')

    while True:
        opcao = input('Deseja continuar com as perguntas? S para Sim ou N para Não.\n').lower()
        if opcao not in ['s', 'n']:
            print('Responda com S para Sim ou N para Não.')
            continue
        if opcao == 'n':
            quer_continuar = False
            print('Jogo encerrado')
        break


