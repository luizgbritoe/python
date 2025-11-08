def calculadora (num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num1 != 0 and num2 != 0:
            return num1 / num2
        else:
            return "Divisão por 0 não pode ser efetuada"
    else:
        return "Operação inválida"
    
resultado = calculadora(10, 2, '/')
print(f'Resultado: {resultado}')