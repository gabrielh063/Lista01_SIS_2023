# Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final.

sli = float(input('Informe o seu salário inicial: '))
sla = sli * 0.15
sla1 = sla + sli
slip = sla * 0.08
sla2 = sla1 - slip
print(f'O sálario inicial é de: {sli}; com o acréscimo de 15%: {sla1}; e com os desconto dos impostos: {sla2};')