// Scriptable widget — Módulo 12 (Controle Glicêmico)
// Calcula taxa de variação, sugere ajuste de insulina e percentual de tempo na meta.

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
    const glicemiaAtual = await promptNumber("Glicemia atual", 210);
    const glicemiaAnterior = await promptNumber("Glicemia anterior", 180);
    const intervalo = await promptNumber("Intervalo (h)", 1);
    const taxaAtual = await promptNumber("Taxa insulina (U/h)", 2);
    const pausas = await promptNumber("Pausa dieta (min)", 0);
    const leituras = await promptNumber("% leituras na meta (estimativa)", 65);

    if (intervalo <= 0) throw new Error("Intervalo deve ser positivo");
    const variacaoHora = (glicemiaAtual - glicemiaAnterior) / intervalo;
    let novaTaxa = taxaAtual;
    if (variacaoHora > 60) novaTaxa += 2;
    else if (variacaoHora > 30) novaTaxa += 1;
    else if (variacaoHora < -40) novaTaxa = Math.max(taxaAtual - 2, 0);
    else if (variacaoHora < -20) novaTaxa = Math.max(taxaAtual - 1, 0);

    let taxaPausa = taxaAtual;
    if (pausas > 0 && pausas <= 120) taxaPausa = taxaAtual * 0.5;
    else if (pausas > 120) taxaPausa = 0;

    const tempoMeta = Math.min(Math.max(leituras, 0), 100);

    const resumo = `Δ/h: ${variacaoHora.toFixed(1)} mg/dL\nNova taxa sugerida: ${novaTaxa.toFixed(1)} U/h\nTaxa se dieta pausa: ${taxaPausa.toFixed(1)} U/h\nTempo na meta: ${tempoMeta.toFixed(0)}%`;
    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(14, 16, 14, 16);
      widget.addText("Controle Glicêmico").font = Font.boldSystemFont(13);
      widget.addSpacer(4);
      widget.addText(`Δ/h: ${variacaoHora.toFixed(1)}`).font = Font.systemFont(12);
      widget.addText(`Nova taxa: ${novaTaxa.toFixed(1)} U/h`).font = Font.systemFont(12);
      widget.addText(`Tempo meta: ${tempoMeta.toFixed(0)}%`).font = Font.systemFont(12);
      const status = widget.addText(tempoMeta >= 70 ? "✅ Meta adequada" : "⚠️ Revisar protocolo");
      status.font = Font.systemFont(10);
      status.textColor = tempoMeta >= 70 ? Color.green() : Color.orange();
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Ajuste de insulina";
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
