// Scriptable widget for Module 08 — Advanced Arterial Access
// Estimates hemodynamic metrics and monitors distal perfusion.

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

function interpretPerfusion(spo2Distal, tempDiff) {
  const notes = [];
  if (spo2Distal < 92) {
    notes.push("SpO₂ distal <92% — avaliar isquemia");
  } else {
    notes.push("SpO₂ distal adequada");
  }
  if (tempDiff > 3) {
    notes.push("ΔT >3°C — aliviar curativo/avaliar fluxo");
  }
  return notes;
}

async function main() {
  try {
    const map = await promptNumber("PAM atual (mmHg)", 70);
    const pic = await promptNumber("PIC (opcional) para CPP (mmHg)", 18);
    const spo2 = await promptNumber("SpO₂ distal (%)", 96);
    const tempDiff = await promptNumber("Diferença de temperatura membro (°C)", 1.5);

    const cpp = map - pic;
    const notes = interpretPerfusion(spo2, tempDiff);
    if (cpp < 60) {
      notes.push("CPP <60 mmHg — revisar suporte hemodinâmico");
    }

    const message = `Monitorização arterial:\n• PAM: ${map.toFixed(1)} mmHg\n• PPC estimada: ${cpp.toFixed(1)} mmHg\n• SpO₂ distal: ${spo2}%\n• ΔT: ${tempDiff.toFixed(1)} °C\n\nAlertas:\n${notes.join("\n")}`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("Acesso Arterial");
      title.font = Font.boldSystemFont(13);
      widget.addSpacer(6);
      widget.addText(`PPC: ${cpp.toFixed(1)} mmHg`).font = Font.systemFont(12);
      widget.addText(`SpO₂ distal: ${spo2}%`).font = Font.systemFont(12);
      widget.addSpacer(6);
      notes.slice(0, 2).forEach(line => {
        const t = widget.addText(line);
        t.font = Font.systemFont(10);
        t.textColor = Color.gray();
      });
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo acesso arterial";
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
