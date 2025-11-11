// Scriptable widget for Module 09 — Fluid Balance Control
// Calculates cumulative balance, FO% and suggests daily targets.

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

function fractionOverload(balance, weight) {
  return (balance / weight) * 100;
}

async function main() {
  try {
    const weight = await promptNumber("Peso ideal (kg)", 70);
    const balance72 = await promptNumber("Balanço acumulado 72h (mL)", 6000);
    const targetRemoval = await promptNumber("Meta remoção hoje (mL)", 1500);
    const diuresis = await promptNumber("Diurese atual (mL/h)", 40);

    const foPercent = fractionOverload(balance72, weight * 1000);
    const messageLines = [
      `Peso ideal: ${weight} kg`,
      `Balanço 72h: ${(balance72 / 1000).toFixed(1)} L`,
      `Fração de sobrecarga: ${foPercent.toFixed(1)}%`,
      `Meta de remoção: ${(targetRemoval / 1000).toFixed(1)} L/24h`,
      `Diurese atual: ${diuresis} mL/h`
    ];
    if (foPercent > 10) {
      messageLines.push("⚠️ Sobrecarga crítica — considerar ultrafiltração");
    }
    if (diuresis < 30) {
      messageLines.push("⚠️ Diurese baixa — avaliar diurético sequencial");
    }

    const message = messageLines.join("\n");

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("Balanço Hídrico");
      title.font = Font.boldSystemFont(13);
      widget.addSpacer(6);
      widget.addText(`FO: ${foPercent.toFixed(1)}%`).font = Font.systemFont(12);
      widget.addText(`Meta: ${(targetRemoval / 1000).toFixed(1)} L`).font = Font.systemFont(12);
      widget.addSpacer(6);
      if (foPercent > 10 || diuresis < 30) {
        const alertText = widget.addText("Revisar plano");
        alertText.font = Font.systemFont(10);
        alertText.textColor = Color.red();
      } else {
        const ok = widget.addText("Dentro do alvo");
        ok.font = Font.systemFont(10);
        ok.textColor = Color.green();
      }
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Plano de balanço";
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
