# escreva um programa que converta uma temperatura em graus C° para F° e vice e versa.
c = int(input('Qual a temperatura: Cº'))
f = ((9 * c) / 5) + 32
print('A temperatura atual de {}ºC convertida para fahrenheit {:.0f}ºF'.format(c, f))
print('#' * 30)
f = int(input('Digote a temperatura em F°:'))
c = (f - 32) * 5 / 9
print('A temperatura em Fahrenheit {}ºF convertida em celcius é {}ºC'.format(f, c))
