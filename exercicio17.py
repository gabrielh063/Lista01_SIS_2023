# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.

cmp = float(input('Informe a quantidade de camisetas pequenas: '))
cmm = float(input('Informe a quantidade de camisetas médias: '))
cmg = float(input('Informe a quantidade de camisetas grandes: '))
cmmp = cmp * 10
cmmm = cmm * 12 
cmmg = cmg * 15
total = cmmp + cmmm + cmmg 
print(f'O total será de R${total}')