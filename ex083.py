expressao = input("Digite a expressão:  ")
pilha = []
for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if not pilha:
            print("A expressão está incorreta.")
            break
        pilha.pop()
else:
    if not pilha:
        print("A expressão está correta.")
    else:
        print("A expressão está incorreta.")
