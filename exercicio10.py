#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.
nv = input('Digite o nome do funcionário: ')
slfx = float(input('Digite o seu sálario: '))
tve = float(input('Digite o total de vendas efetuads em dinheiro: '))
slf = tve * 0.15
print(f'O funcionario {nv} vendeu {tve} esse mês, portanto seu salario de R${slfx} ')
print(f'terá um acréscimo de {slf} por sua comissão de 15%')
print('-'*70)
