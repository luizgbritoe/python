print('***** TABUADA *****')

num = int(input('Digite um número para consultar sua tabuada: '))

print(f'--- Tabuada do {num} ---')
for i in range(1, 11):
    result = num * i
    print(f'{num} * {i} = {result}')
