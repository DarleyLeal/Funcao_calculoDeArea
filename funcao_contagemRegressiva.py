def contador():
    print('          CONTADOR')
    print('-' * 30)
    passo1 = int(input('Inicio: '))
    passo2 = int(input('Passo: '))
    passo3 = int(input('Fim: '))
    for c in range(passo1, passo2, passo3):
        print(f'Contagem de {passo1} até {passo3} de {passo2} em {passo2}')
        print(f'{c}')
        c += 1

contador()
