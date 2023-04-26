# escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto

km = int(input('Digite a distancia percorrida: '))
cb = float(input("Digite a quantidade de combustivel gasto: "))
md = km / cb
print('-'*40)
print(f'A media de combustivel por quilometro é de {md}kmpl')