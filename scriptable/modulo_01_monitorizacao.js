// Scriptable widget for Module 01 — Invasive Hemodynamic Monitoring
// Provides quick calculators and decision hints at the bedside.

const DEFAULT_TARGET = 65; // mmHg

async function promptNumber(prompt, defaultValue) {
  const alert = new Alert();
  alert.title = prompt;
  alert.message = "Informe um valor numérico";
  alert.addTextField("", defaultValue ? String(defaultValue) : "");
  alert.addAction("Ok");
  alert.addCancelAction("Cancelar");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  const value = parseFloat(alert.textFieldValue(0).replace(',', '.'));
  if (isNaN(value)) throw new Error("Valor inválido para " + prompt);
  return value;
}

function calcMAP(sys, dia) {
  return dia + (sys - dia) / 3;
}

function classifyPerfusion(map, lactate, uo) {
  const status = [];
  if (map >= DEFAULT_TARGET) {
    status.push("PAM ≥ meta (" + map.toFixed(1) + " mmHg)");
  } else {
    status.push("PAM abaixo da meta");
  }
  if (lactate < 2) {
    status.push("Lactato adequado");
  } else if (lactate < 4) {
    status.push("Lactato elevado");
  } else {
    status.push("Lactato muito elevado");
  }
  if (uo >= 0.5) {
    status.push("Débito urinário preservado");
  } else {
    status.push("Débito urinário baixo");
  }
  return status.join(" · ");
}

async function main() {
  try {
    const sys = await promptNumber("Pressão arterial sistólica (mmHg)", 120);
    const dia = await promptNumber("Pressão arterial diastólica (mmHg)", 70);
    const lactate = await promptNumber("Lactato (mmol/L)", 2.5);
    const uo = await promptNumber("Débito urinário (mL/kg/h)", 0.4);

    const map = calcMAP(sys, dia);
    const perfusion = classifyPerfusion(map, lactate, uo);

    const message = `PAM calculada: ${map.toFixed(1)} mmHg\n${perfusion}\n\nSugestões rápidas:\n• Reavalie curva arterial e zero do transdutor.\n• Considere ajustes de volume/vasoativos se meta não atingida.\n• Revise metas específicas em cardiopatas ou crônicos.`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const header = widget.addText("Monitorização Invasiva");
      header.font = Font.boldSystemFont(14);
      header.textColor = Color.blue();

      widget.addSpacer(8);
      const pamLine = widget.addText(`PAM: ${map.toFixed(1)} mmHg`);
      pamLine.font = Font.systemFont(16);

      const perfLine = widget.addText(perfusion);
      perfLine.font = Font.systemFont(12);
      perfLine.textColor = Color.gray();

      widget.addSpacer(12);
      const note = widget.addText("Toque para atualizar");
      note.font = Font.italicSystemFont(10);
      note.textColor = Color.darkGray();

      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo hemodinâmico";
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
