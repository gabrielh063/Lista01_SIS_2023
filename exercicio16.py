# O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a balança já desconte o peso do prato.

pspt = float(input('Informe o peso de comida: '))
psdv = pspt / 1000
vlrpt = psdv / 19 
print(f'O valor do prato é de {vlrpt}')
