from main import somar, subtrair, multiplicar, dividir


def teste_somar():
    # 1 - Configurar
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executar
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Validar
    assert resultado_obtido == resultado_esperado


def teste_subtrair():
    # 1 - Configurar
    numero_a = 15
    numero_b = 5
    resultado_esperado = 10

    # 2 - Executar
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Validar
    assert resultado_obtido == resultado_esperado


def teste_multiplicar():
    # 1 - Configurar
    numero_a = 5
    numero_b = 5
    resultado_esperado = 25

    # 2 - Executar
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Validar
    assert resultado_obtido == resultado_esperado


def teste_dividir():
    # 1 - Configurar
    numero_a = 20
    numero_b = 2
    resultado_esperado = 10

    # 2 - Executar
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Validar
    assert resultado_obtido == resultado_esperado


def teste_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 0

    # 1.2 - Resultados Esperados
    resultado_esperado = 'Não dividiras por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado