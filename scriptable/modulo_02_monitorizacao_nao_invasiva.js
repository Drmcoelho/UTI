// Scriptable widget for Module 02 — Non-invasive Hemodynamic Monitoring
// Provides averaging of oscillometric readings and perfusion index alerts.

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

function calcularMedia(valores) {
  return valores.reduce((acc, v) => acc + v, 0) / valores.length;
}

function calcularPAM(sis, dia) {
  return dia + (sis - dia) / 3;
}

function analisarPerfusao(pi, pam) {
  const status = [];
  if (pi >= 1.4) {
    status.push("PI adequado");
  } else {
    status.push("PI baixo — investigar hipoperfusão");
  }
  if (pam >= 65) {
    status.push("PAM ≥ 65 mmHg");
  } else {
    status.push("PAM < 65 mmHg");
  }
  return status.join(" · ");
}

async function main() {
  try {
    const sisValores = [];
    const diaValores = [];
    for (let i = 1; i <= 3; i++) {
      sisValores.push(await promptNumber(`PAS leitura ${i} (mmHg)`, i === 1 ? 86 : undefined));
      diaValores.push(await promptNumber(`PAD leitura ${i} (mmHg)`, i === 1 ? 58 : undefined));
    }
    const pi = await promptNumber("Índice de perfusão (%)", 1.2);
    const vti = await promptNumber("VTI TSV (cm)", 14);
    const area = await promptNumber("Área TSV (cm²)", 3.1);
    const fc = await promptNumber("Frequência cardíaca (bpm)", 96);

    const sisMedia = calcularMedia(sisValores);
    const diaMedia = calcularMedia(diaValores);
    const pam = calcularPAM(sisMedia, diaMedia);
    const volumeSistolico = area * vti;
    const debito = (volumeSistolico * fc) / 1000;
    const perfusao = analisarPerfusao(pi, pam);

    const mensagem = `PAM média: ${pam.toFixed(1)} mmHg\nPI: ${pi.toFixed(1)}%\nDébito estimado: ${debito.toFixed(2)} L/min\n${perfusao}\n\nSugestões:\n• Repetir medidas se diferença > 5 mmHg.\n• Integrar ecocardiografia para revisão do VTI.\n• Converter para monitorização invasiva se sinais discrepantes persistirem.`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const header = widget.addText("Monitorização Não Invasiva");
      header.font = Font.boldSystemFont(14);
      header.textColor = Color.orange();

      widget.addSpacer(8);
      widget.addText(`PAM: ${pam.toFixed(1)} mmHg`).font = Font.systemFont(16);
      widget.addText(`PI: ${pi.toFixed(1)}%`).font = Font.systemFont(12);
      widget.addText(`DC: ${debito.toFixed(2)} L/min`).font = Font.systemFont(12);

      widget.addSpacer(10);
      widget.addText(perfusao).font = Font.systemFont(10);

      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo não invasivo";
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
