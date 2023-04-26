A = input('Digite aqui o nome do aluno: ')
B = float(input('Digite a sua média na prova de portguês: ')) 
C = float(input('Digite a sua média na prova de matemática: '))
D = float(input('Digite a sua média na prova de inglês: '))
E = B + C + D
F = E / 3
print('-'*35)
if (F>= 6):
    print(f'Parabéns sua média é de: {F}') 
else:
    print(f'Que pena, sua média foi de: {F}')
