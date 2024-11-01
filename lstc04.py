import random 
import time
lista = []
jogos = []
total = 1
j = int(input('Digite quantos jogos serão gerados: '))
jg = 0
while total <= j:
    cont = 0
    jg += 1
    while True:
        n = random.randint(0,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6 :
            break
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-='*70)
for i, l in enumerate(jogos):
    print(f'O jogo {i+1} é: {l}')
    time.sleep(1)
print('-='*70)