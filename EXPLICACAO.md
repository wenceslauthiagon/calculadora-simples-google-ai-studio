# Explicação da Calculadora Simples

> Guia para quem está começando em programação.

---

## 1. Principais componentes do código

### Variáveis
Armazenam valores que o programa usa ao longo da execução. Em `calculadora.py`, `a` e `b` guardam os números digitados e `resultado` guarda o valor calculado:
```python
a = ler_numero("  Primeiro número : ")
b = ler_numero("  Segundo número  : ")
resultado = funcao(a, b)
```

### Funções
Blocos de código com nome próprio que podem ser chamados várias vezes. Cada operação tem sua própria função — recebe dois valores e retorna o resultado, sem depender de nada externo:
```python
def soma(a, b):
    return a + b

def divisao(a, b):
    if b == 0:
        return None
    return a / b
```

### Condições (`if` / `else`)
Permitem que o programa tome decisões diferentes dependendo da situação:
```python
if resultado is None:
    print("  [ERRO] Divisao por zero nao e permitida.")
else:
    print(f"  Resultado: {resultado}")
```

### Loop (`while True`)
Mantém o menu rodando até o usuário escolher sair. O `break` encerra o loop:
```python
while True:
    opcao = input("Opção: ")
    if opcao == "5":
        break
```

### Dicionário
Estrutura que associa uma chave a um valor. Aqui mapeia a opção digitada diretamente à função correspondente, eliminando vários `if/elif`:
```python
operacoes = {
    "1": ("Soma",          soma),
    "2": ("Subtração",     subtracao),
    "3": ("Multiplicação", multiplicacao),
    "4": ("Divisão",       divisao),
}
```

---

## 2. Como a aplicação recebe os números e identifica a operação

### Versão CLI (`calculadora.py`)
1. `input("Opção: ")` captura o texto digitado.
2. O programa verifica se o texto é uma chave válida do dicionário `operacoes`.
3. A função `ler_numero()` lê cada número, troca vírgula por ponto e converte com `float()`. Se o usuário digitar letras, o `try/except` captura o erro e pede novamente — sem travar.

### Versão Web (`web/app.py` + `web/static/js/script.js`)
1. O usuário preenche os campos e clica em **Calcular**.
2. O JavaScript envia os dados para o servidor via `fetch("/calcular", { method: "POST" })`.
3. O Flask recebe o JSON, chama `parse_numero()` para converter os valores e identifica a operação pela chave recebida no campo `"operacao"`.

---

## 3. Como a lógica realiza os cálculos e apresenta os resultados

1. **Seleção da função** — `nome_op, funcao = operacoes[opcao]` extrai a função do dicionário.
2. **Execução** — `resultado = funcao(a, b)` chama a função com os dois operandos.
3. **Divisão por zero** — `divisao()` retorna `None` quando `b == 0`; o código checa isso e exibe a mensagem de erro.
4. **Formatação** — se o resultado não tiver parte decimal (ex.: `6.0`), é exibido como inteiro (`6`). Caso contrário, remove zeros desnecessários com `:.6g` na CLI ou `round()` na API.

Na versão web, o resultado volta do servidor em JSON e o JavaScript atualiza a tela dinamicamente, sem recarregar a página.

---

## 4. Cenários de uso

| # | Entrada | Saída esperada |
|---|---|---|
| 1 | Opção `1`, números `5` e `3` | `Soma: 5.0 → 3.0 = 8` |
| 2 | Opção `2`, números `10` e `4,5` | `Subtração: 10.0 → 4.5 = 5.5` |
| 3 | Opção `3`, números `-2` e `6` | `Multiplicação: -2.0 → 6.0 = -12` |
| 4 | Opção `4`, números `7` e `0` | `[ERRO] Divisao por zero nao e permitida.` |
| 5 | Opção `9` (inexistente) | `[!] Opcao invalida. Digite um numero de 1 a 5.` |
| 6 | Número inválido: `abc` | `[!] Entrada invalida. Digite um numero (ex.: 3, -1.5 ou 2,7).` |

---

## 5. Arquitetura da versão web

```
Navegador                     Servidor Flask
─────────                     ──────────────
index.html  ←── renderiza ──  app.py  /
script.js   ──── POST ──────► app.py  /calcular
                               └─ importa calculadora.py
                               └─ chama soma / divisao / ...
            ◄──── JSON ──────  retorna { "resultado": 42 }
style.css   ←── estático ───  static/css/style.css
```

O `calculadora.py` funciona como uma **biblioteca compartilhada**: a CLI e o servidor web importam as mesmas funções, sem duplicar nenhuma lógica.
