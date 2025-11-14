// Scriptable widget — Módulo 14 (Bloqueio Neuromuscular)
// Classifica TOF/postetânico e sugere ajustes.

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

function classificarTOF(tof, postet) {
  if (tof === 0) {
    if (isNaN(postet)) return "Medir contagem postetânica";
    if (postet <= 1) return "Bloqueio muito profundo";
    if (postet <= 3) return "Bloqueio adequado";
    return "Recuperação em curso";
  }
  if (tof <= 2) return "Dentro da meta";
  if (tof === 3) return "Bloqueio superficial";
  return "Sem bloqueio";
}

async function main() {
  try {
    const tof = await promptNumber("Respostas TOF", 1);
    const postet = await promptNumber("Contagem postetânica", 2);
    const pam = await promptNumber("PAM", 70);
    const pic = await promptNumber("PIC", 18);

    const classificacao = classificarTOF(tof, postet);
    const ppc = pam - pic;
    const alertaPPC = ppc < 60 ? "⚠️ PPC baixa" : "✅ PPC adequada";

    const mensagem = `TOF: ${tof} | Postetânica: ${postet}\n${classificacao}\nPPC: ${ppc.toFixed(0)} mmHg (${alertaPPC})`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(12, 12, 12, 12);
      widget.addText("Bloqueio NM").font = Font.boldSystemFont(13);
      widget.addText(`${classificacao}`).font = Font.systemFont(12);
      widget.addText(`PPC: ${ppc.toFixed(0)} mmHg`).font = Font.systemFont(12);
      const status = widget.addText(alertaPPC);
      status.font = Font.systemFont(11);
      status.textColor = alertaPPC.startsWith("⚠️") ? Color.orange() : Color.green();
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Avaliação do bloqueio";
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
