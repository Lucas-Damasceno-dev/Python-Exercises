v = input('Digite algo: ')
print('1- A letra digitada é minuscula? {}. \n'
      '2- É uma letra do alfabeto? {}. \n'
      '3- Contém apenas caracteres alfanuméricos? {}. \n'
      '4- Contém caracteres da ASCII? {}. \n'
      '5- Existem dígitos na string? {}. \n'
      '6- Existem caracteres decimais? {}. \n'
      '7- É um identificador Python? {}. \n'
      '8- É um número? {}. \n'
      '9- É tem um caractere imprimível? {}. \n'
      '10- É um espaço em branco? {}. \n'
      '11- Contém caracteres maiusculos e menusculos? {}. \n'
      '12- Contém caracteres maiusculos? {}. \n'

      .format(v.islower(), v.isalpha(), v.isalnum(), v.isascii(), v.isdigit(), v.isdecimal(), v.isidentifier(), v.isnumeric(), v.isprintable(), v.isspace(), v.istitle(), v.isupper()))