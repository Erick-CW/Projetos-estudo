# Escreva um programa que pergunte a quandidade de km percorridos por um veículo alugado e a quantidade de dias pelos quais foram alugados. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0.15 por km rodados!
print('                    Bem vindo ao Simulador de valores')
km = float(input('Quantos km deseja percorrer:'))
diaria = int(input('Por quantos dias você quer alugar:'))
calckm = km * 0.15
calcd = diaria * 60
print('De acordo com os dados informado: \nTotal da diária: R${:.2f} \nTotal de km: R${:.2f} \n>>>>>>>>Preço total a pagar: R${:.2f}<<<<<<<<<'.format(calcd, calckm, calckm + calcd))