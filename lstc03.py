lista1 = []
lista2 = []
lista3 = []
s = 0
s1 = 0
dados = []
for c in range(0,3):
    n = int(input('Digite um número para a 1ª linha: '))
    if c == 2 :
        s1 += n
    if n % 2 == 0 :
        s += n
    dados.append(n)
    lista1.append(dados[:]) 
    dados.clear()
for d in range(0,3):
    n = int(input('Digite um número para a 2ª linha: '))
    if d == 2 :
        s1 += n
    if n % 2 == 0 :
        s += n
    dados.append(n)
    lista2.append(dados[:])
    dados.clear()
for e in range(0,3):
    n = int(input('Digite um número para a 2ª linha: '))
    if e == 2 :
        s1 += n
    if n % 2 == 0 :
        s += n
    dados.append(n)
    lista3.append(dados[:])
    dados.clear()

print(lista1[0],lista1[1],lista1[2])
print(lista2[0],lista2[1],lista2[2])
print(lista3[0],lista3[1],lista3[2])
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da terceira coluna é: {s1}')
print(f'O maior valora da segunda linha é {max(lista2)}')