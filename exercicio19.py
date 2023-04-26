# A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra

qnt = int(input('Digite a quantidade de sanduiches a serem feitos: '))
q =  qnt * 100 / 1000
p = qnt * 50 / 1000
h = qnt * 100 / 1000
print(f'para fazer {qnt} serão necessários:')
print(f'{q:.2f}kg de queijo')
print(f'{p:.2f}kg de presunto')
print(f'{h:.2f}kg de hamburguer')