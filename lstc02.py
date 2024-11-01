listan = [[],[]]
print('-='*70)
for c in range(0,7) :
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        listan[0].append(n)
        print('Número adicionado!')
    else:
        listan[1].append(n)
        print('Número adicionado!')
listan[0].sort()
listan[1].sort()
print('-='*70)
print(f'Os valores ímpares em ordem crescente são: {listan[1]}')
print(f'Os valores pares em ordem crescente são: {listan[0]}')
print('-='*70)
    
    