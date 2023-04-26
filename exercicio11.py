# Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.

dp = float(input('Digite o valor depositado: '))
print('-'*40)
rd = dp * 0.0070
print(f'O rendimento mensal do seu depósito é de: {rd} reais ao mês')
print('-'*40)