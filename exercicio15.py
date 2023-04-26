# Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: Tibúrcio, você já viveu 6935 dias.

nm = input('Digite o seu nome: ')
idd = int(input('Digite sua idade: '))
iddd = idd * 365 
print(f'{nm} ja viveu {iddd} dias')