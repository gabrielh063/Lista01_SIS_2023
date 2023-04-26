# Um motorista deseja colocar no tanque do seu carro X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
pcg = 5.65
pg = float(input('Qual o valor do pagamento: '))
ltc = pg / pcg
print(f'você colocou {ltc:.2f} litros de gasolina')
print('-'*40)