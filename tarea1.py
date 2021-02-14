import random
import modulo
print('Bienvenido al juego!')
print('Seleccione un numero\nPiedra = 0\nPapel = 1\nTijera = 2')
opciones = ['Piedra', 'Papel', 'Tijera']
entrada = int(input("Ingresa seleccion:"))
tuseleccion = opciones[entrada]
pcseleccion = opciones[random.randrange(0, 3)]
print ('Has elegido',tuseleccion, 'y la pc', pcseleccion)
modulo.ganador(tuseleccion,pcseleccion)
print('Juego Finalizado')