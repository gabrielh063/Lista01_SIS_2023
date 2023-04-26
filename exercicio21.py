# Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças. Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante a liquidação?'

a = float(input('Digite o preço da peça: '))
b = a * 0.30
c = a - b
print(f'O preço da peça é de {a} e com o desconto ficará {c:.2f}')