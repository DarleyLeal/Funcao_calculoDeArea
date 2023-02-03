def area():
    print('\033[1;33m         CONTROLE DE TERRENOS\033[m')
    print('-' * 40)
    larg = float(input('LARGURA: '))
    comp = float(input('COMPRIMENTO: '))
    print(f'A área de um terreno {larg} x {comp} é {larg * comp}m²')

area()


