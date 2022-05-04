import pytest

def imprimir_oi(nome):
    print(f'Oi, {nome}')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividirás por zero'


if __name__ == '__main__':
    imprimir_oi('Nunes')

    resultado = somar(15, 5)
    print(f'A soma é: {resultado}')
    resultado = subtrair(15, 5)
    print(f'A substração é: {resultado}')
    resultado = multiplicar(5, 5)
    print(f'A multiplicação é: {resultado}')
    resultado = dividir(20, 2)
    print(f'A divisão é: {resultado}')









