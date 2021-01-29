# Converter  moedas cotação com dados de 20/01/21.
real = float(input('Quanto dinheiro você tem na carteira? R$: '))
dolar = real / 5.34
peso = real / 0.0616
euro = real / 6.451
libra = real / 7.267
iene = real / 0.509
print('Com R$:{:.2f} reais, da para comprar: \n{:.2f} dollar, \npeso {:.2f}, \neuro {:.2f}, \nlibra {:.2f} e \niene {:.2f}. '.format(real, dolar, peso, euro, libra, iene))


