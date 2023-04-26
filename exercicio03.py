# o custo ao consumidor de um carro novo é a soma do custo de fabrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fabrica). supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fabrica de um carro e escreva o custo ao consumidor

""" o custo do consumidor de um carro novo SOMA 

custo de fabricaçao com a % do distribuidor e dos impostos

Percentagem distribuidor 28% 
percentagem impostos 45% 

custo consumidor 30.000 
""" 
ctfb = float(input('Digite o valor de fabricaçao do carro:'))
ctds = 0.28*ctfb
ip = 0.45*ctfb
ctcs = ctfb + ctds + ip
print('-'*30)
print(f'o custo ao consumidor é R${ctcs}')
