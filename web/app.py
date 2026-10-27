from flask import Flask, render_template, request, jsonify
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from calculadora import soma, subtracao, multiplicacao, divisao

app = Flask(__name__)

OPERACOES = {
    "soma":          soma,
    "subtracao":     subtracao,
    "multiplicacao": multiplicacao,
    "divisao":       divisao,
}

def parse_numero(valor):
    return float(str(valor).replace(",", "."))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()

    try:
        a = parse_numero(dados["a"])
        b = parse_numero(dados["b"])
    except (ValueError, KeyError):
        return jsonify({"erro": "Número inválido."}), 400

    op = dados.get("operacao")
    if op not in OPERACOES:
        return jsonify({"erro": "Operação inválida."}), 400

    resultado = OPERACOES[op](a, b)

    if resultado is None:
        return jsonify({"erro": "Divisão por zero não é permitida."}), 400

    valor = int(resultado) if resultado == int(resultado) else round(resultado, 10)
    return jsonify({"resultado": valor})

if __name__ == "__main__":
    app.run(debug=True)
