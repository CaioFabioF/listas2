temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o seu nome: ')))
    temp.append(float(input('Digite o seu peso: ')))
    if len(princ) == 0 :
        mai = men = temp[1]
    else:
        if temp[1] > mai :
            mai = temp[1]
        if temp[1] < men :
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if continuar in 'Nn' :
        break
print('-='*70)
print(f'Os dados cadastrados foram: {princ}.')
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi {mai}')
for p in princ :
    if p[1] == mai:
        print(f'O maior peso foi de {p[0]}')
print(f'O menor peso foi {men}')
for p in princ :
    if p[1] == men:
        print(f'O menor peso foi de {p[0]}')
