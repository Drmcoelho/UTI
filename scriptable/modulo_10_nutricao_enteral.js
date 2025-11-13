// Scriptable widget for Module 10 — Enteral Nutrition
// Computes caloric/protein targets and tracks infusion progress.

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
    const weight = await promptNumber("Peso (kg)", 75);
    const kcalPerKg = await promptNumber("Calorias alvo (kcal/kg)", 30);
    const proteinPerKg = await promptNumber("Proteína alvo (g/kg)", 1.8);
    const formulaDensity = await promptNumber("Densidade fórmula (kcal/mL)", 1.2);
    const infused = await promptNumber("Volume infundido últimas 24h (mL)", 1400);

    const totalKcal = weight * kcalPerKg;
    const totalProtein = weight * proteinPerKg;
    const requiredVolume = totalKcal / formulaDensity;
    const coverage = (infused / requiredVolume) * 100;

    const message = `Metas diárias:\n• Calorias: ${totalKcal.toFixed(0)} kcal\n• Proteína: ${totalProtein.toFixed(0)} g\n• Volume alvo: ${requiredVolume.toFixed(0)} mL\nVolume infundido: ${infused} mL (${coverage.toFixed(0)}%)\n${coverage < 80 ? "⚠️ Aumentar ritmo/ajustar interrupções" : "✅ Meta adequada"}`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("Nutrição Enteral");
      title.font = Font.boldSystemFont(13);
      widget.addSpacer(6);
      widget.addText(`Alvo kcal: ${totalKcal.toFixed(0)}`).font = Font.systemFont(12);
      widget.addText(`Cobertura: ${coverage.toFixed(0)}%`).font = Font.systemFont(12);
      widget.addSpacer(6);
      const status = widget.addText(coverage < 80 ? "Ajustar dieta" : "Dentro da meta");
      status.font = Font.systemFont(10);
      status.textColor = coverage < 80 ? Color.red() : Color.green();
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Plano nutricional";
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
