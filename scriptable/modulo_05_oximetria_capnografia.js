// Scriptable widget for Module 05 — Oximetria e Capnografia
// Provides quick assessment of SpO2, perfusion index and ETCO2 gradient.

async function promptNumber(prompt, defaultValue) {
  const alert = new Alert();
  alert.title = prompt;
  alert.addTextField("", defaultValue ? String(defaultValue) : "");
  alert.addAction("Ok");
  alert.addCancelAction("Cancelar");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  const value = parseFloat(alert.textFieldValue(0).replace(',', '.'));
  if (isNaN(value)) throw new Error(`Valor inválido para ${prompt}`);
  return value;
}

function evaluateOximetry(spo2, pi) {
  const msgs = [];
  if (spo2 < 92) msgs.push("SpO₂ baixa");
  else if (spo2 > 98) msgs.push("SpO₂ alta");
  else msgs.push("SpO₂ ok");

  if (pi < 0.5) msgs.push("PI <0,5% — confiabilidade baixa");
  else if (pi < 1) msgs.push("PI moderado");
  else msgs.push("PI adequado");
  return msgs.join(" · ");
}

function gradientStatus(etco2, paco2) {
  const gradient = paco2 - etco2;
  if (gradient < 0) return { gradient, status: "ETCO₂ > PaCO₂ (verificar calibração)" };
  if (gradient <= 10) return { gradient, status: "Gradiente ok" };
  return { gradient, status: ">10 mmHg — avaliar espaço morto" };
}

async function main() {
  try {
    const spo2 = await promptNumber("SpO₂ (%)", 94);
    const pi = await promptNumber("Índice de perfusão (%)", 1.1);
    const etco2 = await promptNumber("ETCO₂ (mmHg)", 35);
    const paco2 = await promptNumber("PaCO₂ (mmHg)", 40);
    const co2insp = await promptNumber("CO₂ inspiratório (mmHg)", 1);
    const retornoBase = await promptNumber("Curva retorna à linha de base? 1=Sim / 0=Não", 1);

    const oxiMsg = evaluateOximetry(spo2, pi);
    const gradInfo = gradientStatus(etco2, paco2);
    const reinalacao = !retornoBase && co2insp > 3 ? "Possível reinalação" : "Retorno adequado";

    const summary = `SpO₂ ${spo2}% (${oxiMsg})\nETCO₂ ${etco2} vs PaCO₂ ${paco2} → Δ ${gradInfo.gradient.toFixed(1)}\n${gradInfo.status}\n${reinalacao}`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("Oximetria & Capnografia");
      title.font = Font.boldSystemFont(13);
      widget.addSpacer(6);
      widget.addText(`SpO₂ ${spo2}% | PI ${pi}%`).font = Font.systemFont(12);
      widget.addText(oxiMsg).font = Font.systemFont(10);
      widget.addSpacer(4);
      widget.addText(`ΔETCO₂ ${gradInfo.gradient.toFixed(1)} mmHg`).font = Font.systemFont(12);
      widget.addText(gradInfo.status).font = Font.systemFont(10);
      widget.addSpacer(4);
      widget.addText(reinalacao).font = Font.systemFont(10);
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo monitorização";
      alert.message = summary;
      alert.addAction("OK");
      await alert.present();
    }
  } catch (error) {
    if (error.message !== "Operação cancelada") {
      const alert = new Alert();
      alert.title = "Erro";
      alert.message = error.message;
      alert.addAction("OK");
      await alert.present();
    }
  }
}

await main();
