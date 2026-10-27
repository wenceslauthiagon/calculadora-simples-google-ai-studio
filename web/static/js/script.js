const SIMBOLOS = {
  soma:          "+",
  subtracao:     "−",
  multiplicacao: "×",
  divisao:       "÷",
};

let opSelecionada = null;

document.querySelectorAll(".op-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".op-btn").forEach(b => b.classList.remove("ativo"));
    btn.classList.add("ativo");
    opSelecionada = btn.dataset.op;
  });
});

document.getElementById("btn-calcular").addEventListener("click", async () => {
  const a = document.getElementById("num-a").value.trim();
  const b = document.getElementById("num-b").value.trim();

  if (!a || !b)       return mostrar("erro", "Preencha os dois campos.");
  if (!opSelecionada) return mostrar("erro", "Escolha uma operação.");

  const resp = await fetch("/calcular", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ a, b, operacao: opSelecionada }),
  });

  const dados = await resp.json();

  if (dados.erro) {
    mostrar("erro", dados.erro);
  } else {
    mostrar("sucesso", `${a} ${SIMBOLOS[opSelecionada]} ${b}`, dados.resultado);
  }
});

function mostrar(tipo, expressao, valor) {
  const el = document.getElementById("resultado");
  el.className = tipo;
  el.style.display = "block";

  if (tipo === "sucesso") {
    el.innerHTML = `
      <div class="label-res">${expressao}</div>
      <div class="valor-res">${valor}</div>
    `;
  } else {
    el.textContent = expressao;
  }
}
