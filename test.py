lp = []
d = []
maior = 0
pmp = []
pml = []
while True:
    d.append(str(input('Nome: ')))
    d.append(int(input('Peso: ')))
    lp.append(d[:])
    d.clear()
    while True:
        q = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if q == 'S' or q == 'N':
            break
        else:
            print('Tente novamente.')
    if q == 'N':
        break
for i in lp:
    if i[1] > maior or i[1] == maior:
        maior = i[1]
for i in lp:
    if i[1] == maior:
        pmp.append(i[0])
menor = lp[0][1]
for i in lp:
    if i[1] < menor or i[1] == menor:
        menor = i[1]
for i in lp:
    if i[1] == menor:
        pml.append(i[0])
print(f'{len(lp)} pessoas foram cadastras.')
print(f'A(s) pessoa(s) mais pesada(s) da lista: {pmp}')
print(f'A(s) pessoa(s) mais leve(s) da lista: {pml}')
