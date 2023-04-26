#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

vlpd = float(input('Digite o preço do produto: '))
vlpt = vlpd / 5
print('-'*40)
print(f'o valor de cada parcela é de R${vlpt} ao mês')
