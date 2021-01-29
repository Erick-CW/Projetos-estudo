# faça um programa que leia um ângulo qualquer e mostre ma tela o valor de seno, cosseno e tangente.
import math
ang = float(input('Digite um ângulo qualquer:'))
s = math.sin(math.radians(ang)) # Calcula o Seno
c = math.cos(math.radians(ang)) # Calcula a Cosseno
t = math.tan(math.radians(ang)) # Calcula a Tangente
print('O Seno do ângulo de {:.2f} tem o Seno {:.2f}, Cosseno {:.2f} e sua Tangente {:.2f}'.format(ang, s, c, t))





