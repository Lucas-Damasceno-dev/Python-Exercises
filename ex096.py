def area(largura, comprimento):
    return largura * comprimento


largura = float(input('LARGURA (m):  '))
comprimento = float(input('COMPRIMENTO (m):  '))
area_do_terreno = area(largura, comprimento)
print(f'A área de um terreno {largura}x{comprimento} é de {area_do_terreno:.2f}m²')
