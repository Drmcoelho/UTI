// Scriptable widget for Module 03 — Pulmonary Artery Catheter
// Summarizes hemodynamic calculations and readiness to remove the catheter.

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

function indiceCardiaco(debito, superficie) {
  if (superficie <= 0) throw new Error("SC inválida");
  return debito / superficie;
}

function resistenciaVascular(pam, pad, debito) {
  if (debito <= 0) throw new Error("Débito inválido");
  return 80 * (pam - pad) / debito;
}

function classificarFenotipo(ic, pcp) {
  if (ic < 2.2 && pcp > 18) return "Choque cardiogênico congestivo";
  if (ic < 2.2) return "Choque cardiogênico com pré-carga adequada";
  if (pcp < 8) return "Hipovolemia provável";
  return "Perfusão estável";
}

function prontoParaRetirada(ic, svo2, lactato, pam) {
  return ic >= 2.2 && svo2 >= 65 && lactato <= 2 && pam >= 65;
}

async function main() {
  try {
    const pad = await promptNumber("PAD (mmHg)", 18);
    const papm = await promptNumber("PAP média (mmHg)", 31);
    const pcp = await promptNumber("PCP (mmHg)", 28);
    const debito = await promptNumber("Débito cardíaco (L/min)", 3.0);
    const superficie = await promptNumber("Superfície corporal (m²)", 1.9);
    const pam = await promptNumber("PAM invasiva (mmHg)", 63);
    const svo2 = await promptNumber("SvO₂ (%)", 60);
    const lactato = await promptNumber("Lactato (mmol/L)", 1.8);

    const ic = indiceCardiaco(debito, superficie);
    const rvs = resistenciaVascular(pam, pad, debito);
    const rvp = resistenciaVascular(papm, pcp, debito);
    const fenotipo = classificarFenotipo(ic, pcp);
    const retirada = prontoParaRetirada(ic, svo2, lactato, pam);

    const mensagem = `IC: ${ic.toFixed(2)} L/min/m²\nRVS: ${rvs.toFixed(0)} dyn·s·cm⁻⁵\nRVP: ${rvp.toFixed(0)} dyn·s·cm⁻⁵\nFenótipo: ${fenotipo}\nPronto para retirar CAP? ${retirada ? 'Sim' : 'Não'}\n\nChecklist:\n• Verifique curvas e balão antes de registrar PCP.\n• Ajuste vasopressores evitando RVS > 1200.\n• Reavalie metas a cada 4-6h.`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const header = widget.addText("Cateter Artéria Pulmonar");
      header.font = Font.boldSystemFont(14);
      header.textColor = Color.red();

      widget.addSpacer(8);
      widget.addText(`IC: ${ic.toFixed(2)} L/min/m²`).font = Font.systemFont(13);
      widget.addText(`RVS: ${rvs.toFixed(0)}`).font = Font.systemFont(12);
      widget.addText(`Fenótipo: ${fenotipo}`).font = Font.systemFont(10);
      widget.addSpacer(6);
      widget.addText(retirada ? "Pronto para retirar" : "Manter CAP").font = Font.boldSystemFont(11);

      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo CAP";
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
