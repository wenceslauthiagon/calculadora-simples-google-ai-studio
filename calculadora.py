# Calculadora de linha de comando com as quatro operações básicas

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

# Dicionário que mapeia a opção do menu para a função correspondente
operacoes = {
    "1": ("Soma",           soma),
    "2": ("Subtração",      subtracao),
    "3": ("Multiplicação",  multiplicacao),
    "4": ("Divisão",        divisao),
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
        print("  5. Sair")

        opcao = input("\nOpção: ").strip()

        # Verifica se o usuário quer sair
        if opcao == "5":
            print("Até logo!")
            break

        # Verifica se a opção é válida
        if opcao not in operacoes:
            print("  [!] Opcao invalida. Digite um numero de 1 a 5.")
            continue

        nome_op, funcao = operacoes[opcao]

        # Lê os dois operandos
        a = ler_numero("  Primeiro número : ")
        b = ler_numero("  Segundo número  : ")

        resultado = funcao(a, b)

        # Trata divisão por zero
        if resultado is None:
            print("  [ERRO] Divisao por zero nao e permitida.")
        else:
            # Exibe inteiro quando não há parte decimal
            if resultado == int(resultado):
                print(f"\n  {nome_op}: {a} → {b} = {int(resultado)}")
            else:
                print(f"\n  {nome_op}: {a} → {b} = {resultado:.6g}")

if __name__ == "__main__":
    main()
