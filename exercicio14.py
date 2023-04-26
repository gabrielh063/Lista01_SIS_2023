# A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança.

pao = int(input('Quantos pães foram vendidos: '))
bolo = float(input('Quantos pedaços foram vendidos: '))

vdp = pao * 0.12 
vdbl = bolo * 1.50
vdtl = vdp + vdbl 
pp = vdp + vdbl * 0.10
 
print(f'O faturamento foi R${vdtl}, sendo R${vdp} de pães e R${vdbl} de pedaços de bolo')
print(f'O total de dinheiro guardado na poupança foi de R${pp}')
