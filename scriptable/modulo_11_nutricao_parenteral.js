// Scriptable widget — Módulo 11 (Nutrição Parenteral Total)
// Calcula peso ajustado, metas calóricas e alerta para triglicerídeos.

async function promptNumber(title, defaultValue) {
  const alert = new Alert();
  alert.title = title;
  alert.addTextField("", defaultValue !== undefined ? String(defaultValue) : "");
  alert.addAction("OK");
  alert.addCancelAction("Cancelar");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  const value = parseFloat(alert.textFieldValue(0).replace(',', '.'));
  if (isNaN(value)) throw new Error(`Valor inválido para ${title}`);
  return value;
}

function pesoAjustado(pesoAtual, imcAtual, imcAlvo, altura) {
  return pesoAtual + (imcAlvo - imcAtual) * (altura ** 2);
}

async function main() {
  try {
    const pesoAtual = await promptNumber("Peso atual (kg)", 64);
    const altura = await promptNumber("Altura (m)", 1.7);
    const imcAtual = await promptNumber("IMC atual", 21);
    const imcAlvo = await promptNumber("IMC alvo", 22);
    const kcalKg = await promptNumber("kcal/kg", 30);
    const proteinaKg = await promptNumber("Proteína g/kg", 1.8);
    const triglicerideos = await promptNumber("Triglicerídeos (mg/dL)", 180);
    const horas = await promptNumber("Horas de infusão", 24);

    const pesoAj = pesoAjustado(pesoAtual, imcAtual, imcAlvo, altura);
    const kcalTotais = pesoAj * kcalKg;
    const proteinaTotal = pesoAj * proteinaKg;
    const carbo = kcalTotais * 0.6;
    const lipidio = kcalTotais * 0.2;
    const volume = (carbo / 3.4) + (proteinaTotal / 0.2) + (lipidio / 2);
    const ritmo = volume / horas;
    const alertaTG = triglicerideos >= 500 ? "❌ Suspender lipídio" : (triglicerideos >= 400 ? "⚠️ Reduzir lipídio" : "✅ TG em faixa segura");

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(14, 16, 14, 16);
      widget.addText("NPT — Peso ajustado").font = Font.boldSystemFont(13);
      widget.addSpacer(4);
      widget.addText(`Peso aj.: ${pesoAj.toFixed(1)} kg`).font = Font.systemFont(12);
      widget.addText(`Kcal: ${kcalTotais.toFixed(0)} / dia`).font = Font.systemFont(12);
      widget.addText(`Ritmo: ${ritmo.toFixed(0)} mL/h`).font = Font.systemFont(12);
      const status = widget.addText(alertaTG);
      status.font = Font.systemFont(10);
      status.textColor = alertaTG.startsWith("❌") ? Color.red() : (alertaTG.startsWith("⚠️") ? Color.orange() : Color.green());
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Plano de NPT";
      alert.message = `Peso ajustado: ${pesoAj.toFixed(1)} kg\nCalorias: ${kcalTotais.toFixed(0)} kcal/dia\nProteína: ${proteinaTotal.toFixed(0)} g/dia\nCarboidratos: ${carbo.toFixed(0)} kcal\nLipídios: ${lipidio.toFixed(0)} kcal\nVolume estimado: ${volume.toFixed(0)} mL\nRitmo necessário: ${ritmo.toFixed(0)} mL/h\n${alertaTG}`;
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
