"""Quiz interativo e banco de questões do módulo 03 (cateter de artéria pulmonar)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem='Indicação e planejamento do cateter de artéria pulmonar',
        subquestions=('Quais perfis hemodinâmicos se beneficiam do Swan-Ganz?', 'Quais exames laboratoriais e imagem devem anteceder o procedimento?', 'Como elaborar checklist de segurança com a equipe?'),
        guidance='Utilizar em choque cardiogênico, choque misto refratário, hipertensão pulmonar complexa e pós-operatório de cirurgia cardíaca de alto risco. Solicitar coagulograma, hemograma, eletrólitos, radiografia de tórax e ecocardiograma recente. Checklist inclui verificação de materiais, calibragem de transdutores, monitor multiparamétrico, marcapasso externo e analgesia/sedação adequada.',
    ),
    EssayPrompt(
        stem='Interpretação integrada das curvas e parâmetros derivados',
        subquestions=('Como diferenciar curva de artéria pulmonar e PCP?', 'Quais valores sugerem choque cardiogênico versus distributivo?', 'Como correlacionar SvO₂, lactato e índice cardíaco?'),
        guidance="Curva de artéria pulmonar apresenta incisura dicrótica; PCP possui morfologia atrial com 'a' e 'v'. RVS elevada com PCP > 18 mmHg aponta cardiogênico; PCP baixa e RVS baixa indicam distributivo. SvO₂ < 60% com IC < 2,2 L/min/m² e lactato elevado reforçam hipoperfusão.",
    ),
    EssayPrompt(
        stem='Estratégias para retirada segura do cateter',
        subquestions=('Quais metas clínicas e laboratoriais devem ser atingidas?', 'Como monitorar sinais de complicação durante a retirada?', 'Que documentação e educação ao time são necessários após remoção?'),
        guidance='Exigir PAM ≥ 65-70 mmHg sem escalonamento, IC ≥ 2,2 L/min/m², SvO₂ ≥ 65%, PCP adequada (< 18 mmHg) e lactato < 2 mmol/L. Monitorar arritmias, resistência durante tração e sangramento. Documentar horário, medidas finais, condições do paciente e orientações para vigilância nas próximas horas.',
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt='Qual sequência correta para a passagem do cateter de artéria pulmonar?',
        options=('Introdução na veia femoral → átrio direito → ventrículo direito → artéria pulmonar → wedge', 'Introdução na veia subclávia → ventrículo direito → átrio direito → artéria pulmonar', 'Introdução na veia jugular → artéria pulmonar → ventrículo direito → átrio direito', 'Introdução na veia femoral → átrio direito → artéria pulmonar → ventrículo esquerdo', 'Introdução na veia subclávia → artéria pulmonar → wedge → ventrículo esquerdo'),
        correct_index=0,
        difficulty='básico',
        explanation='A sequência habitual é átrio direito, ventrículo direito, artéria pulmonar e oclusão (PCP) com balão insuflado ao final.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual das situações abaixo contraindica temporariamente a inserção do CAP?',
        options=('Paciente com uso de anticoagulação profilática', 'Bloqueio de ramo esquerdo prévio', 'Choque cardiogênico com ECMO', 'Hipotermia terapêutica', 'Uso de drogas inotrópicas'),
        correct_index=1,
        difficulty='básico',
        explanation='CAP pode precipitar bloqueio AV completo em pacientes com BRE; considerar marca-passo temporário antes da passagem.',
    ),
    MultipleChoiceQuestion(
        prompt='PCP 26 mmHg, RVS 1.400 dyn·s·cm⁻⁵ e IC 1,8 L/min/m² sugerem',
        options=('Choque distributivo', 'Choque cardiogênico', 'Hipovolemia', 'Choque obstrutivo', 'Situação normal'),
        correct_index=1,
        difficulty='intermediário',
        explanation='PCP elevada, RVS alta e IC baixo caracterizam choque cardiogênico com congestão pulmonar importante.',
    ),
    MultipleChoiceQuestion(
        prompt='Durante insuflação do balão, a curva apresenta onda ventriculosa sustentada. Conduta imediata?',
        options=('Prosseguir com a insuflação até desaparecer', 'Desinsuflar imediatamente e recuar 1-2 cm', 'Aumentar fluxo de oxigênio', 'Administrar vasodilatador pulmonar', 'Retirar cateter e reinserir pelo outro lado'),
        correct_index=1,
        difficulty='intermediário',
        explanation='Onda ventriculosa indica posicionamento em ventrículo direito; desinsuflar e reposicionar para evitar perfuração.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual cálculo correto da RVS considerando PAM 70 mmHg, PVC 12 mmHg, DC 4 L/min?',
        options=('RVS = 80 × (PAM − PVC) / DC', 'RVS = PAM / DC', 'RVS = (PAM × DC) / 80', 'RVS = 60 × (PVC − PAM) / DC', 'RVS = (PAM − PVC) × DC'),
        correct_index=0,
        difficulty='avançado',
        explanation='A fórmula padrão é RVS = 80 × (PAM − PVC) / DC, resultando em 1.040 dyn·s·cm⁻⁵ nesse exemplo.',
    ),
    MultipleChoiceQuestion(
        prompt='Queda abrupta da SvO₂ para 52% com IC estável sugere',
        options=('Aumento do consumo de oxigênio', 'Erro de calibração', 'Aumento do débito cardíaco', 'Perfuração de artéria pulmonar', 'Tamponamento cardíaco'),
        correct_index=0,
        difficulty='avançado',
        explanation='SvO₂ reduzida com IC estável indica aumento do consumo (febre, agitação) ou queda na saturação arterial; investigar causa clínica.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual achado sugere hipertensão pulmonar pré-capilar?',
        options=('PCP 26 mmHg e PAP média 28 mmHg', 'PCP 12 mmHg e PAP média 35 mmHg', 'PCP 8 mmHg e PAP média 20 mmHg', 'PCP 18 mmHg e PAP média 24 mmHg', 'PCP 10 mmHg e PAP média 22 mmHg'),
        correct_index=1,
        difficulty='difícil',
        explanation='PAP média ≥ 25 mmHg com PCP ≤ 15 mmHg caracteriza hipertensão pulmonar pré-capilar; PAP 35 e PCP 12 cumprem o critério.',
    ),
    MultipleChoiceQuestion(
        prompt='Quando considerar retirada do CAP após estabilização?',
        options=('Após redução de lactato, mas ainda em altas doses de vasopressor', 'Quando critérios clínicos e hemodinâmicos estáveis ≥ 24h sem ajustes', 'Imediatamente após normalizar a SvO₂', 'Quando o paciente inicia mobilização passiva', 'Assim que o débito urinário melhora'),
        correct_index=1,
        difficulty='extremo',
        explanation='Retirada segura ocorre após 24h sem ajustes, com metas de PAM, PCP, SvO₂ e IC consolidadas e sem novas intervenções planejadas.',
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement='PCP representa estimativa indireta da pressão de átrio esquerdo.',
        is_true=True,
        rationale='Em condições sem obstrução, PCP reflete pressão diastólica final do ventrículo esquerdo.',
    ),
    VFStatement(
        statement='Balão deve permanecer insuflado continuamente para prevenir deslocamento.',
        is_true=False,
        rationale='Balão deve ser desinsuflado após a medida; insuflação contínua aumenta risco de isquemia pulmonar.',
    ),
    VFStatement(
        statement='SvO₂ < 60% com lactato elevado sugere aporte insuficiente de oxigênio.',
        is_true=True,
        rationale='Combinação indica má perfusão e deve levar à otimização de débito ou oferta de O₂.',
    ),
    VFStatement(
        statement='PVC elevada isoladamente confirma sobrecarga de volume.',
        is_true=False,
        rationale='PVC isolada é inespecífica; é necessário integrar com outros parâmetros e exame físico.',
    ),
    VFStatement(
        statement="A curva wedge normal possui ondas 'a' e 'v' proeminentes.",
        is_true=True,
        rationale='Formato atrial ajuda a diferenciar de curva ventricular durante posicionamento.',
    ),
    VFStatement(
        statement='Injetar solução fria no termistor permite calcular débito cardíaco por termodiluição.',
        is_true=True,
        rationale='A queda de temperatura registrada produz curva utilizada no cálculo do débito.',
    ),
    VFStatement(
        statement='RVS baixa e PCP alta caracterizam choque distributivo.',
        is_true=False,
        rationale='Choque distributivo cursa com PCP baixa; PCP alta sugere componente cardiogênico.',
    ),
    VFStatement(
        statement='O CAP não deve ser utilizado em pacientes com prótese valvar.',
        is_true=False,
        rationale='Próteses não contraindicam; considerar risco individual e técnica apurada.',
    ),
    VFStatement(
        statement='Hipertensão pulmonar severa aumenta risco de ruptura arterial durante passagem do cateter.',
        is_true=True,
        rationale='Fragilidade vascular e pressões elevadas elevam risco de hemorragia.',
    ),
    VFStatement(
        statement='Ao inflar o balão, o volume máximo recomendado é 1,5 mL.',
        is_true=True,
        rationale='Exceder 1,5 mL aumenta risco de ruptura vascular e wedge falso.',
    ),
    VFStatement(
        statement='Índice cardíaco é calculado dividindo o débito cardíaco pela superfície corporal.',
        is_true=True,
        rationale='IC (L/min/m²) permite comparar débito ajustado ao tamanho corporal.',
    ),
    VFStatement(
        statement='Se a curva wedge não aparece, deve-se avançar o cateter com balão desinsuflado.',
        is_true=False,
        rationale='Avançar desinsuflado aumenta risco de perfuração; avançar com balão insuflado de forma controlada.',
    ),
    VFStatement(
        statement='CAP fornece medidas contínuas de saturação venosa mista quando equipado com fibra óptica.',
        is_true=True,
        rationale='Modelos modernos oferecem SvO₂ contínua para trending em tempo real.',
    ),
    VFStatement(
        statement='Após retirada, é dispensável monitorar o sítio de inserção.',
        is_true=False,
        rationale='É obrigatório monitorar sangramento, hematoma e sinais de infecção nas horas seguintes.',
    ),
    VFStatement(
        statement='Elevação súbita da pressão de artéria pulmonar pode indicar oclusão do cateter.',
        is_true=True,
        rationale='Revisar posicionamento e descartar trombo ou looping do cateter.',
    ),
)

def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 03 — Cateter de Artéria Pulmonar (Swan-Ganz) ===")
    print("Questões de múltipla escolha")
    run_mcq_session(MCQ_QUESTIONS)
    print("\nAfirmativas verdadeiro/falso")
    run_vf_session(VF_STATEMENTS)

if __name__ == "__main__":
    executar_interativo()

__all__ = ["ESSAY_PROMPTS", "MCQ_QUESTIONS", "VF_STATEMENTS", "resumo_banco", "executar_interativo"]
