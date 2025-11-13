// Scriptable widget — Módulo 13 (Sedação e Analgesia)
// Avalia metas de RASS/CPOT e risco de triglicerídeos elevados.

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

async function main() {
  try {
    const rass = await promptNumber("RASS atual", -3);
    const cpot = await promptNumber("CPOT atual", 4);
    const triglicerideos = await promptNumber("Triglicerídeos", 380);

    let statusRass = "Dentro da meta";
    if (rass < -2) statusRass = "Sedação profunda";
    else if (rass > 0) statusRass = "Sedação insuficiente";

    const statusCpot = cpot > 3 ? "Dor mal controlada" : "Analgesia adequada";
    const statusTG = triglicerideos >= 500 ? "❌ Suspender propofol" : (triglicerideos >= 400 ? "⚠️ Reduzir propofol" : "✅ TG OK");

    const resumo = `RASS: ${rass} (${statusRass})\nCPOT: ${cpot} (${statusCpot})\nTriglicerídeos: ${triglicerideos} (${statusTG})`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(12, 14, 12, 14);
      widget.addText("Sedoanalgesia").font = Font.boldSystemFont(13);
      widget.addText(`RASS ${rass} (${statusRass})`).font = Font.systemFont(12);
      widget.addText(`CPOT ${cpot} (${statusCpot})`).font = Font.systemFont(12);
      const tg = widget.addText(statusTG);
      tg.font = Font.systemFont(11);
      tg.textColor = statusTG.startsWith("❌") ? Color.red() : (statusTG.startsWith("⚠️") ? Color.orange() : Color.green());
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Avaliação de Sedação";
      alert.message = resumo;
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
