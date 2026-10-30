# Testes simples para a calculadora (sem pytest, somente asserts)

from calculadora import soma, subtracao, multiplicacao, divisao, porcentagem

def testar_soma():
    assert soma(2, 3) == 5,           "soma(2, 3) deve ser 5"
    assert soma(-1, 1) == 0,          "soma(-1, 1) deve ser 0"
    assert soma(0.5, 0.5) == 1.0,     "soma(0.5, 0.5) deve ser 1.0"
    assert soma(-3, -7) == -10,       "soma(-3, -7) deve ser -10"
    print("  [OK] soma")

def testar_subtracao():
    assert subtracao(10, 4) == 6,     "subtracao(10, 4) deve ser 6"
    assert subtracao(0, 5) == -5,     "subtracao(0, 5) deve ser -5"
    assert subtracao(-2, -3) == 1,    "subtracao(-2, -3) deve ser 1"
    assert subtracao(1.5, 0.5) == 1,  "subtracao(1.5, 0.5) deve ser 1"
    print("  [OK] subtracao")

def testar_multiplicacao():
    assert multiplicacao(3, 4) == 12,       "multiplicacao(3, 4) deve ser 12"
    assert multiplicacao(-2, 5) == -10,     "multiplicacao(-2, 5) deve ser -10"
    assert multiplicacao(0, 999) == 0,      "multiplicacao(0, 999) deve ser 0"
    assert multiplicacao(1.5, 2) == 3.0,    "multiplicacao(1.5, 2) deve ser 3.0"
    print("  [OK] multiplicacao")

def testar_divisao():
    assert divisao(10, 2) == 5.0,           "divisao(10, 2) deve ser 5.0"
    assert divisao(-9, 3) == -3.0,          "divisao(-9, 3) deve ser -3.0"
    assert divisao(1, 4) == 0.25,           "divisao(1, 4) deve ser 0.25"
    assert divisao(5, 0) is None,           "divisao(5, 0) deve retornar None"
    assert divisao(0, 0) is None,           "divisao(0, 0) deve retornar None"
    print("  [OK] divisao")

def testar_porcentagem():
    import math
    assert porcentagem(10, 200) == 20,                        "10% de 200 deve ser 20"
    assert porcentagem(50, 80)  == 40,                        "50% de 80 deve ser 40"
    assert porcentagem(0, 500)  == 0,                         "0% de qualquer valor deve ser 0"
    assert porcentagem(100, 75) == 75,                        "100% de um valor deve ser o proprio valor"
    assert math.isclose(porcentagem(12.5, 80), 10),           "12.5% de 80 deve ser 10"
    assert porcentagem(-10, 200) == -20,                      "-10% de 200 deve ser -20"
    assert porcentagem(10, -200) == -20,                      "10% de -200 deve ser -20"
    print("  [OK] porcentagem")

if __name__ == "__main__":
    print("Executando testes...\n")
    testar_soma()
    testar_subtracao()
    testar_multiplicacao()
    testar_divisao()
    testar_porcentagem()
    print("\nTodos os testes passaram!")
