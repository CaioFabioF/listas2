matriz = [[0,0,0],[0,0,0],[0,0,0]]
s = 0
s3 = 0
print('-='*70)
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor: '))
        if matriz[l][c] % 2 == 0 :
            s += matriz[l][c]
        if c == 2 :
            s3 += matriz[l][c]
print('-='*70)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print(f'A soma dos valores pares foi {s}')
print(f'A soma dos valores da terceira coluna foi {s3}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')
print('-='*70)
