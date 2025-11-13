// Scriptable widget for Module 04 — POCUS
// Calculates stroke volume, cardiac output and suggests hemodynamic phenotype.

async function promptNumber(prompt, defaultValue) {
  const alert = new Alert();
  alert.title = prompt;
  alert.addTextField("", defaultValue ? String(defaultValue) : "");
  alert.addAction("Ok");
  alert.addCancelAction("Cancelar");
  const response = await alert.presentAlert();
  if (response === -1) throw new Error("Operação cancelada");
  const value = parseFloat(alert.textFieldValue(0).replace(',', '.'));
  if (isNaN(value)) throw new Error(`Valor inválido para ${prompt}`);
  return value;
}

function calcStrokeVolume(diametroCm, vtiCm) {
  const radius = diametroCm / 2;
  const area = Math.PI * Math.pow(radius, 2);
  return area * vtiCm; // mL
}

function classifyVolumeStatus(vti, ivcDiameter, ivcCollapse, controlledVentilation) {
  const msgs = [];
  if (vti < 18) msgs.push("VTI baixo");
  else if (vti > 22) msgs.push("VTI alto");
  else msgs.push("VTI dentro da faixa");

  if (controlledVentilation) {
    if (ivcCollapse < 12 && ivcDiameter > 2.1) msgs.push("IVC tensa");
    else if (ivcCollapse > 18) msgs.push("IVC sugere hipovolemia");
    else msgs.push("IVC adequada");
  } else {
    if (ivcCollapse > 50) msgs.push("Hipovolemia provável");
    else if (ivcDiameter > 2.1 && ivcCollapse < 30) msgs.push("Alta pressão de enchimento");
    else msgs.push("IVC sem achados críticos");
  }
  return msgs.join(" · ");
}

async function main() {
  try {
    const diametro = await promptNumber("Diâmetro LVOT (cm)", 2.0);
    const vti = await promptNumber("VTI LVOT (cm)", 18);
    const fc = await promptNumber("Frequência cardíaca (bpm)", 90);
    const tapse = await promptNumber("TAPSE (mm)", 18);
    const ivcDiam = await promptNumber("Diâmetro IVC (cm)", 2.0);
    const ivcCollapse = await promptNumber("Colapso IVC (%)", 20);
    const controlled = await promptNumber("Ventilação controlada? 1=Sim / 0=Não", 1);

    const sv = calcStrokeVolume(diametro, vti);
    const co = (sv * fc) / 1000;
    const tapseStatus = tapse < 17 ? "Disfunção VD" : tapse > 24 ? "Hiperdinamismo VD" : "VD preservado";
    const volumeStatus = classifyVolumeStatus(vti, ivcDiam, ivcCollapse, controlled >= 0.5);

    const summary = `VS: ${sv.toFixed(1)} mL\nDC: ${co.toFixed(2)} L/min\nTAPSE: ${tapse} mm (${tapseStatus})\n${volumeStatus}`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("POCUS Hemodinâmico");
      title.font = Font.boldSystemFont(14);
      widget.addSpacer(8);
      const line1 = widget.addText(`VS ${sv.toFixed(0)} mL | DC ${co.toFixed(2)} L/min`);
      line1.font = Font.systemFont(12);
      const line2 = widget.addText(`TAPSE ${tapse} mm (${tapseStatus})`);
      line2.font = Font.systemFont(12);
      const line3 = widget.addText(volumeStatus);
      line3.font = Font.systemFont(10);
      line3.textColor = Color.gray();
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo POCUS";
      alert.message = summary;
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
