"""Quiz interativo e banco de questões do módulo 06 (monitorização da PIC)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem="Crise de PIC refratária durante manejo de TCE grave",
        subquestions=(
            "Quais parâmetros devem ser avaliados imediatamente (PIC, PPC, PRx, PbtO₂)?",
            "Como reorganizar o bundle básico antes de iniciar terapias de resgate?",
            "Quais critérios definem escalonamento para barbitúrico ou craniectomia descompressiva?",
        ),
        guidance="\n".join(
            [
                "Reavaliar PIC, PPC (PAM - PIC), índice de autorregulação (PRx) e PbtO₂ quando disponível.",
                "Antes de terapias de resgate, otimizar cabeça a 30°, alinhar cervical, garantir sedação/analgesia profunda, ventilação controlada com PaCO₂ 35 mmHg e drenar líquor se cateter ventricular.",
                "Escalonar quando PIC > 25 mmHg por > 1 h apesar de bundle completo, PPC < 60 mmHg ou deterioro clínico/imagem com sinais de herniação.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Integração da monitorização multimodal",
        subquestions=(
            "Como correlacionar dados de doppler transcraniano com tendências de PIC?",
            "Quais ajustes realizar quando PRx > 0,3 sugerindo perda de autorregulação?",
            "Como comunicar achados e decisões durante rounds multiprofissionais?",
        ),
        guidance="\n".join(
            [
                "Doppler avalia fluxo médio e pulsatilidade; aumento do índice de pulsatilidade com PIC elevada sugere congestão intracraniana.",
                "PRx > 0,3 indica perda de autorregulação — ajustar metas de PAM para otimizar PPC, evitar hipercapnia e considerar terapia osmótica.",
                "Documentar resumo diário com gráficos de PIC/PPC, intervenções e resposta, alinhando metas com neurocirurgia, enfermagem e fisioterapia.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Prevenção de infecção associada ao cateter de PIC",
        subquestions=(
            "Quais medidas de inserção estéril são mandatórias?",
            "Como deve ser o protocolo de manutenção diária?",
            "Quando remover o cateter e quais passos seguir após remoção?",
        ),
        guidance="\n".join(
            [
                "Checklist de barreira máxima, antibiótico profilático conforme protocolo neurocirúrgico e confirmação radiológica quando indicado.",
                "Manutenção com curativo estéril transparente trocado a cada 72h ou se sujo, manipulação mínima com técnica estéril e flush conforme fabricante.",
                "Remover após controle da hipertensão intracraniana ou sinais de infecção; enviar ponta para cultura e documentar monitorização pós-retirada.",
            ]
        ),
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Paciente com PIC 28 mmHg e PAM 82 mmHg. Qual PPC e conduta imediata?",
        options=("PPC 54 mmHg; manter conduta", "PPC 110 mmHg; reduzir vasopressor", "PPC 54 mmHg; otimizar bundle básico", "PPC 28 mmHg; iniciar barbitúrico", "PPC 82 mmHg; indicar craniectomia"),
        correct_index=2,
        difficulty="básico",
        explanation="PPC = PAM - PIC = 54 mmHg (abaixo da meta 60-70). Reforçar medidas básicas antes de escalonar para terapias de resgate.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual dos achados abaixo mais sugere necessidade de drenagem imediata de líquor?",
        options=("PRx -0,1", "PbtO₂ 30 mmHg", "Onda B sustentada", "PIC oscilando 20-22 mmHg", "Onda A (plateau) > 5 min"),
        correct_index=4,
        difficulty="intermediário",
        explanation="Ondas A prolongadas refletem elevação sustentada da PIC e baixa complacência, exigindo drenagem ou terapia escalonada urgente.",
    ),
    MultipleChoiceQuestion(
        prompt="Durante aspiração traqueal, PIC sobe de 20 para 32 mmHg. Qual estratégia preventiva?",
        options=("Hiperventilar paciente para PaCO₂ 25 mmHg", "Aumentar PEEP para 12 cmH₂O", "Bolus prévio de remifentanil e lidocaína", "Rebaixar cabeceira para 0°", "Administrar furosemida"),
        correct_index=2,
        difficulty="intermediário",
        explanation="Analgesia e bloqueio simpático com remifentanil e lidocaína minimizam resposta hipertensiva durante aspiração.",
    ),
    MultipleChoiceQuestion(
        prompt="Paciente com PRx 0,4 e PPC 50 mmHg. Melhor conduta inicial?",
        options=("Reduzir PAM alvo para 60 mmHg", "Aumentar sedação e reduzir ventilação", "Elevar PAM alvo para 90 mmHg", "Suspender todas as intervenções", "Administrar dexametasona"),
        correct_index=2,
        difficulty="avançado",
        explanation="PRx alto sugere perda de autorregulação; elevar PAM alvo para melhorar PPC enquanto monitoriza resposta e evita hipercapnia.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual complicação está mais associada a cateter intraparenquimatoso?",
        options=("Hidrocefalia aguda", "Infecção ventriculite", "Drift zero e recalibração limitada", "Hemorragia intraperitoneal", "Hipotensão postural"),
        correct_index=2,
        difficulty="avançado",
        explanation="Cateter parenquimatoso não permite recalibração pós-implantação, levando a drift de zero ao longo dos dias de monitorização.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual alvo de PaCO₂ é recomendado na ausência de sinais de herniação iminente?",
        options=("25-30 mmHg", "30-35 mmHg", "35-40 mmHg", "45-50 mmHg", ">50 mmHg"),
        correct_index=2,
        difficulty="difícil",
        explanation="Hiperventilação profunda só é indicada temporariamente; alvo habitual é PaCO₂ 35-40 mmHg para evitar vasoconstrição cerebral e isquemia.",
    ),
    MultipleChoiceQuestion(
        prompt="Após bolus de solução hipertônica, qual parâmetro deve ser monitorado a cada 2-4h?",
        options=("Amônia sérica", "Sódio plasmático", "Fibrinogênio", "Cálcio iônico", "Creatinina fosfoquinase"),
        correct_index=1,
        difficulty="difícil",
        explanation="Sódio e osmolaridade sérica devem ser monitorados estreitamente para evitar hipernatremia severa e lesão osmótica.",
    ),
    MultipleChoiceQuestion(
        prompt="Paciente com PIC 18 mmHg e PbtO₂ 15 mmHg. Interpretação?",
        options=("Monitorização dentro da normalidade", "Hipoperfusão cerebral apesar de PIC aceitável", "Erro de calibração do cateter", "Hiperventilação excessiva reduzindo PPC", "Necessidade de drenar líquor"),
        correct_index=1,
        difficulty="extremo",
        explanation="PbtO₂ < 20 mmHg indica hipoxia tecidual cerebral mesmo com PIC controlada; revisar PPC, ventilação e oxigenação.",
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement="PPC é calculada pela diferença entre PAM e PIC.",
        is_true=True,
        rationale="PPC = PAM - PIC; alvo usual 60-70 mmHg em TCE grave.",
    ),
    VFStatement(
        statement="Ondas B representam complacência extremamente baixa com risco iminente de herniação.",
        is_true=False,
        rationale="Ondas B são oscilatórias e refletem variações respiratórias/vasomotoras; ondas A (plateau) sinalizam risco maior.",
    ),
    VFStatement(
        statement="Hiperventilação prolongada para PaCO₂ < 30 mmHg é estratégia segura de longo prazo.",
        is_true=False,
        rationale="Hiperventilação profunda pode causar isquemia; usar apenas como ponte em herniação iminente.",
    ),
    VFStatement(
        statement="PRx negativo sugere autorregulação preservada.",
        is_true=True,
        rationale="Índice de autorregulação cerebral negativo indica correlação inversa entre PAM e PIC, sinalizando autoregulação ativa.",
    ),
    VFStatement(
        statement="Craniectomia descompressiva está indicada quando PIC > 20 mmHg por 5 minutos.",
        is_true=False,
        rationale="Indicação envolve PIC refratária > 25 mmHg por tempo prolongado apesar de medidas máximas e correlação clínica/radiológica.",
    ),
    VFStatement(
        statement="Monitorização contínua de temperatura e glicemia faz parte do bundle de PIC.",
        is_true=True,
        rationale="Hiperglicemia e hipertermia aumentam metabolismo cerebral e devem ser controladas.",
    ),
    VFStatement(
        statement="Cateter intraventricular permite drenagem terapêutica e calibração periódica.",
        is_true=True,
        rationale="Ventriculostomia é padrão-ouro por permitir drenagem de líquor e recalibração do zero.",
    ),
    VFStatement(
        statement="Uso de bloqueador neuromuscular é contraindicado em PIC elevada.",
        is_true=False,
        rationale="Bloqueio pode ser útil para controlar tosse e movimentos que elevam PIC; deve ser usado com monitorização adequada.",
    ),
    VFStatement(
        statement="PbtO₂ < 20 mmHg exige otimização da oxigenação e PPC.",
        is_true=True,
        rationale="Meta de PbtO₂ ≥ 20 mmHg está associada a melhores desfechos; revisar ventilação e hemodinâmica.",
    ),
    VFStatement(
        statement="Drift do sensor é inexistente em cateteres de fibra óptica.",
        is_true=False,
        rationale="Cateteres de fibra óptica apresentam drift progressivo e não podem ser recalibrados após implantação.",
    ),
    VFStatement(
        statement="Avaliar posicionamento do cateter após mobilização reduz episódios de leitura falsa.",
        is_true=True,
        rationale="Mudança postural pode deslocar cateter; checar posicionamento e zero após mobilização relevante.",
    ),
    VFStatement(
        statement="Sedação superficial é suficiente para todos os pacientes com PIC elevada.",
        is_true=False,
        rationale="Sedação profunda é frequentemente necessária para controlar estímulos; ajustar conforme resposta e monitorização neurológica.",
    ),
    VFStatement(
        statement="Ondas em dente de serra no doppler transcraniano indicam hiperemia cerebral.",
        is_true=False,
        rationale="Índice de pulsatilidade alto com fluxo reduzido sugere aumento de resistência; hiperemia mostra velocidades elevadas com PI baixo.",
    ),
    VFStatement(
        statement="Controle rigoroso de sódio é fundamental durante terapia com salina hipertônica.",
        is_true=True,
        rationale="Evita hipernatremia grave e síndrome osmótica desmielinizante.",
    ),
    VFStatement(
        statement="Checklist de PIC deve incluir plano de reavaliação com neurocirurgia.",
        is_true=True,
        rationale="Governança multiprofissional reduz variabilidade e melhora segurança do paciente.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 06 — Monitorização da Pressão Intracraniana ===")
    print("Questões de múltipla escolha")
    run_mcq_session(MCQ_QUESTIONS)
    print("\nAfirmativas verdadeiro/falso")
    run_vf_session(VF_STATEMENTS)


if __name__ == "__main__":
    executar_interativo()


__all__ = [
    "ESSAY_PROMPTS",
    "MCQ_QUESTIONS",
    "VF_STATEMENTS",
    "resumo_banco",
    "executar_interativo",
]
