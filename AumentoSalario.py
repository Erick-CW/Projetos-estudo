# fça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15 de aumento.
salario = float(input('Salário atual:R$'))
novo = salario + (salario * 15 / 100)
print(' R${} x 15 / 100 = R$:{}'.format(salario, novo))
print('O salário atual é R${:.2f}, e com o aumento de 15% passa a ser R${:.2f}'.format(salario, novo))
