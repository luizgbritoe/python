print('***** VERIFICADOR DE MAIORIDADE *****')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade>=18:
    print(f'Olá {nome}, você é maior de idade.')
else:
    print(f'Olá {nome}, você é menor de idade.')