pessoas = []
dados = []
totmai = totmen = 0
for c in range(0,3) :
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(int(input('Digite a sua idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print('-='*50)
for a in pessoas :
    print(f'{a[0]} tem {a[1]} anos.')
print('-='*50)
for b in pessoas :
    if b[1] >= 18 :
        print(f'{b[0]} é maior de idade.')
        totmai += 1
    else :
        print(f'{b[0]} é menor de idade.')
        totmen += 1
print('-='*50)
print(f'São {totmai} maiores de idade e {totmen} menores de idade.')
print('-='*50)
