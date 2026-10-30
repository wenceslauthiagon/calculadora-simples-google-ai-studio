# 🧮 Calculadora Simples

Calculadora desenvolvida em **Python 3** com duas interfaces: linha de comando (CLI) e web (Flask). Projeto criado como desafio de programação usando apenas biblioteca padrão na CLI e Flask na versão web.

---

## 📁 Estrutura

```
calculadora-simples/
├── calculadora.py          # lógica das operações e porcentagem (compartilhada)
├── test_calculadora.py     # testes automatizados
├── EXPLICACAO.md           # guia didático para iniciantes
└── web/
    ├── app.py              # servidor Flask
    ├── templates/
    │   └── index.html      # estrutura da página
    └── static/
        ├── css/
        │   └── style.css   # estilos com variáveis CSS
        └── js/
            └── script.js   # lógica do front-end
```

---

## ✨ Funcionalidades

- ➕ Soma · ➖ Subtração · ✖️ Multiplicação · ➗ Divisão · 📊 Porcentagem ("X% de Y")
- Aceita vírgula ou ponto como separador decimal (`1,5` ou `1.5`)
- Trata entradas inválidas sem travar o programa
- Trata divisão por zero com mensagem clara

---

## 🖥️ Versão CLI

### Pré-requisito
```bash
python --version   # Python 3.x
```

### Executar
```bash
python calculadora.py
```

### Exemplo
```
========================================
       CALCULADORA SIMPLES - Python
========================================

Escolha uma operação:
  1. Soma
  2. Subtração
  3. Multiplicação
  4. Divisão
  5. Porcentagem
  6. Sair

Opção: 5
  Percentual (%) : 15
  Valor          : 200

  Porcentagem: 15% de 200 = 30

Opção: 4
  Primeiro número : 10
  Segundo número  : 0

  [ERRO] Divisao por zero nao e permitida.
```

---

## 🌐 Versão Web (Flask)

### Pré-requisito
[uv](https://github.com/astral-sh/uv) instalado.

### Executar
```bash
cd web
uv run --with flask python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 🧪 Testes

Sem dependências externas — usa apenas `assert`:

```bash
python test_calculadora.py
```

```
Executando testes...

  [OK] soma
  [OK] subtracao
  [OK] multiplicacao
  [OK] divisao
  [OK] porcentagem

Todos os testes passaram!
```

Cenários cobertos: operações básicas, porcentagem, decimais, negativos e divisão por zero.

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Lógica | Python 3 (biblioteca padrão) |
| Servidor web | Flask 3 |
| Front-end | HTML + CSS (variáveis) + JavaScript |
