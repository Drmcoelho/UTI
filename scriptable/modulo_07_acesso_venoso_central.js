// Scriptable widget for Module 07 — Central Venous Access
// Tracks bundle adherence and highlights infection risks.

async function promptToggle(prompt) {
  const alert = new Alert();
  alert.title = prompt;
  alert.message = "Selecione uma opção";
  alert.addAction("Sim");
  alert.addAction("Não");
  alert.addCancelAction("Cancelar");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  return response === 0;
}

async function promptNumber(prompt, defaultValue) {
  const alert = new Alert();
  alert.title = prompt;
  alert.addTextField("", defaultValue !== undefined ? String(defaultValue) : "");
  alert.addAction("Ok");
  alert.addCancelAction("Cancelar");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  const value = parseFloat(alert.textFieldValue(0).replace(',', '.'));
  if (isNaN(value)) throw new Error(`Valor inválido para ${prompt}`);
  return value;
}

async function main() {
  try {
    const bundle = await promptToggle("Bundle completo na inserção?");
    const dressingDays = await promptNumber("Dias desde o último curativo", 3);
    const temp = await promptNumber("Temperatura atual (°C)", 37.2);
    const site = await promptToggle("Sinais locais (hiperemia/pus)?");

    const risks = [];
    if (!bundle) risks.push("Reforçar barreira máxima na próxima inserção");
    if (dressingDays > 7) risks.push("Curativo vencido — trocar imediatamente");
    if (site) risks.push("Avaliar retirada do cateter e coletar culturas");
    if (temp >= 38) risks.push("Febre — correlacionar com culturas e outros focos");

    const message = `Checklist CVC:\n• Bundle inserção: ${bundle ? "cumprido" : "falhou"}\n• Dias do curativo: ${dressingDays}\n• Temperatura: ${temp.toFixed(1)} °C\n• Sinais locais: ${site ? "presentes" : "ausentes"}\n\nAlertas:\n${risks.length ? risks.join("\n") : "Nenhum"}`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("CVC Bundle");
      title.font = Font.boldSystemFont(13);
      widget.addSpacer(6);
      widget.addText(`Curativo: ${dressingDays} dias`).font = Font.systemFont(12);
      widget.addText(`Temp.: ${temp.toFixed(1)} °C`).font = Font.systemFont(12);
      widget.addSpacer(6);
      const status = widget.addText(risks.length ? `${risks.length} alerta(s)` : "Sem alertas");
      status.font = Font.systemFont(10);
      status.textColor = risks.length ? Color.red() : Color.green();
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Checklist CVC";
      alert.message = message;
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
