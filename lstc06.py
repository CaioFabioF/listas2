ficha = []
while True :
    nome = str(input('Digite o seu nome: '))
    nota1 = int(input('Digite a sua nota 1: '))
    nota2 = int(input('Digite a sua nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
    if continuar in 'Nn' :
        break
print('-='*50)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-='*50)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-='*50)
    opc = int(input('Deseja mostrar as notas de qual aluno?(999 para finalizar): '))
    if opc == 999 :
        print('Finalizado')
        break
    if opc <= len(ficha) -1 :
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')