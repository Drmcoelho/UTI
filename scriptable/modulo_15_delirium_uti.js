// Scriptable widget — Módulo 15 (Delirium em UTI)
// Avalia CAM-ICU e alerta QTc.

async function promptBoolean(title, defaultValue) {
  const alert = new Alert();
  alert.title = title;
  alert.addAction("Sim");
  alert.addAction("Não");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  return response === 0;
}

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
    const inicioAgudo = await promptBoolean("Início agudo / curso flutuante?", true);
    const inatencao = await promptBoolean("Inatenção presente?", true);
    const pensamento = await promptBoolean("Pensamento desorganizado?", false);
    const consciencia = await promptBoolean("Nível de consciência alterado?", true);
    const qtc = await promptNumber("QTc (ms)", 470);

    const camPositivo = inicioAgudo && inatencao && (pensamento || consciencia);
    let alertaQtc = "QTc dentro da faixa segura";
    if (qtc >= 500) alertaQtc = "❌ Evitar haloperidol";
    else if (qtc >= 470) alertaQtc = "⚠️ Monitorizar QTc diariamente";

    const mensagem = `CAM-ICU: ${camPositivo ? "Positivo" : "Negativo"}\nQTc: ${qtc} ms (${alertaQtc})`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(14, 16, 14, 16);
      widget.addText("Delirium").font = Font.boldSystemFont(13);
      widget.addText(`CAM-ICU ${camPositivo ? "positivo" : "negativo"}`).font = Font.systemFont(12);
      const status = widget.addText(alertaQtc);
      status.font = Font.systemFont(11);
      status.textColor = alertaQtc.startsWith("❌") ? Color.red() : (alertaQtc.startsWith("⚠️") ? Color.orange() : Color.green());
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Avaliação de Delirium";
      alert.message = mensagem;
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
