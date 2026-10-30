# Calculadora de linha de comando com as quatro operações básicas e porcentagem

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna o produto de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de dois números; retorna None se b for zero."""
    if b == 0:
        return None  # Divisão por zero não é permitida
    return a / b

def porcentagem(percentual, valor):
    """Retorna percentual% de valor (ex.: 15% de 200 = 30)."""
    return valor * percentual / 100

# Dicionário que mapeia a opção do menu para a função correspondente
operacoes = {
    "1": ("Soma",           soma),
    "2": ("Subtração",      subtracao),
    "3": ("Multiplicação",  multiplicacao),
    "4": ("Divisão",        divisao),
    "5": ("Porcentagem",    porcentagem),
}

def ler_numero(mensagem):
    """Lê um número do usuário, aceitando vírgula ou ponto como separador decimal."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("  [!] Entrada invalida. Digite um numero (ex.: 3, -1.5 ou 2,7).\n")

def main():
    """Função principal: exibe o menu em loop até o usuário escolher sair."""
    print("=" * 40)
    print("       CALCULADORA SIMPLES - Python")
    print("=" * 40)

    # Loop principal do menu
    while True:
        print("\nEscolha uma operação:")
        for chave, (nome, _) in operacoes.items():
            print(f"  {chave}. {nome}")
        print("  6. Sair")

        opcao = input("\nOpção: ").strip()

        # Verifica se o usuário quer sair
        if opcao == "6":
            print("Até logo!")
            break

        # Verifica se a opção é válida
        if opcao not in operacoes:
            print("  [!] Opcao invalida. Digite um numero de 1 a 6.")
            continue

        nome_op, funcao = operacoes[opcao]

        # Lê os dois operandos
        if opcao == "5":
            a = ler_numero("  Percentual (%) : ")
            b = ler_numero("  Valor          : ")
        else:
            a = ler_numero("  Primeiro número : ")
            b = ler_numero("  Segundo número  : ")

        resultado = funcao(a, b)

        # Trata divisão por zero
        if resultado is None:
            print("  [ERRO] Divisao por zero nao e permitida.")
        else:
            # Exibe inteiro quando não há parte decimal
            simbolo = f"{a}% de {b}" if opcao == "5" else f"{a} → {b}"
            if resultado == int(resultado):
                print(f"\n  {nome_op}: {simbolo} = {int(resultado)}")
            else:
                print(f"\n  {nome_op}: {simbolo} = {resultado:.6g}")

if __name__ == "__main__":
    main()
