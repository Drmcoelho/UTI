// Scriptable widget for Module 06 — Monitorização da PIC
// Calculates CPP, classifies crisis severity and suggests next steps.

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

function classifyPIC(pic, cpp, pbtO2) {
  const status = [];
  status.push(`PIC ${pic.toFixed(1)} mmHg`);
  status.push(`PPC ${cpp.toFixed(1)} mmHg`);
  if (pic >= 25) {
    status.push("⚠️ Crise hipertensiva — reforçar bundle e considerar resgate");
  } else if (pic >= 20) {
    status.push("⚠️ Limite alto — otimizar posição/sedação");
  } else {
    status.push("✅ Dentro da meta (<22 mmHg)");
  }
  if (cpp < 60) {
    status.push("Ajustar PAM alvo para 65-70 mmHg");
  }
  if (pbtO2 && pbtO2 < 20) {
    status.push("PbtO₂ baixo — otimizar oxigenação/perfusão");
  }
  return status;
}

async function main() {
  try {
    const map = await promptNumber("PAM (mmHg)", 80);
    const pic = await promptNumber("PIC (mmHg)", 22);
    const pbt = await promptNumber("PbtO₂ (mmHg) — opcional", 18);
    const sodium = await promptNumber("Sódio sérico (mEq/L)", 150);

    const cpp = map - pic;
    const status = classifyPIC(pic, cpp, pbt);
    if (sodium > 155) {
      status.push("Rever terapia hipertônica (Na > 155 mEq/L)");
    }

    const message = `${status.join("\n")}\n\nPróximos passos sugeridos:\n• Verificar zero e posição do cateter.\n• Revisar sedação/analgesia antes de escalonar.\n• Considerar drenagem de LCR ou solução hipertônica se refratário.`;

    if (config.runsInWidget) {
      const widget = new ListWidget();
      widget.setPadding(16, 16, 16, 16);
      const title = widget.addText("Bundle PIC");
      title.font = Font.boldSystemFont(13);
      widget.addSpacer(6);
      widget.addText(`PIC: ${pic.toFixed(1)} mmHg`).font = Font.systemFont(12);
      widget.addText(`PPC: ${cpp.toFixed(1)} mmHg`).font = Font.systemFont(12);
      widget.addSpacer(6);
      status.slice(2, 4).forEach(line => {
        const t = widget.addText(line);
        t.font = Font.systemFont(10);
        t.textColor = Color.gray();
      });
      widget.addSpacer(6);
      widget.addText(`Na⁺: ${sodium.toFixed(0)} mEq/L`).font = Font.systemFont(10);
      Script.setWidget(widget);
      Script.complete();
    } else {
      const alert = new Alert();
      alert.title = "Resumo PIC";
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
