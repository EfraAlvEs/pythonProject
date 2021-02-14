def ganador(a, b):
    if a == b:
        return print('Empate.')
    elif a == 'Piedra' and b == 'Tijeras':
        return print('Ganaste.')
    elif a == 'Papel' and b == 'Piedra':
        return print('Ganaste.')
    elif a == 'Tijeras' and b == 'Papel':
        return print('Ganaste.')
    else:
        return print('Perdiste.')