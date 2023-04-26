#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

vlct = float(input('Digite o preço de custo do produto: '))
ptac = float(input('Digite a porcetagem do acréscimo: '))
vlvd = vlct * ptac
vlfn = vlct + vlvd
print(f'O valor de venda é de R${vlfn}')