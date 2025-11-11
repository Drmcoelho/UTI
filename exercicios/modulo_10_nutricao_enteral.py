"""Quiz interativo e banco de questões do módulo 10 (nutrição enteral)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem="Planejamento nutricional em paciente de alto risco",
        subquestions=(
            "Como calcular necessidades calóricas e proteicas personalizadas?",
            "Qual estratégia de progressão da dieta para atingir metas em 72h?",
            "Quais indicadores devem ser monitorados diariamente?",
        ),
        guidance="\n".join(
            [
                "Utilizar 25-30 kcal/kg ajustado por calorimetria quando disponível e 1,5-2 g/kg de proteína considerando estresse metabólico.",
                "Progressão escalonada iniciando com 25 mL/h e aumento de 10-20 mL/h a cada 6h se resíduos < 500 mL e hemodinâmica estável.",
                "Monitorar balanço nitrogenado, glicemia, eletrólitos, resíduos gástricos, evacuações, marcadores inflamatórios e peso diário.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Gestão de intolerância gastrointestinal",
        subquestions=(
            "Quais causas avaliar diante de resíduos elevados?",
            "Quais intervenções farmacológicas podem ser utilizadas?",
            "Quando indicar sonda pós-pilórica?",
        ),
        guidance="\n".join(
            [
                "Revisar posicionamento da sonda, uso de opioides/sedação, distúrbios eletrolíticos, íleo e infecções.",
                "Utilizar pró-cinéticos (metoclopramida, eritromicina), ajustar velocidade, considerar naloxona enteral e fórmulas com fibra.",
                "Indicar pós-pilórica se resíduos > 500 mL persistentes, risco de aspiração elevado ou ventilação prolongada.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Integração multiprofissional e documentação",
        subquestions=(
            "Como envolver nutrição, enfermagem e fisioterapia no plano?",
            "Quais registros são mandatórios para rastreabilidade?",
            "Como comunicar interrupções e retomadas da dieta?",
        ),
        guidance="\n".join(
            [
                "Realizar rounds multiprofissionais com metas claras, posicionamento adequado e checklists de tolerância.",
                "Registros obrigatórios incluem volume prescrito/infundido, resíduos, evacuações, eventos adversos e suplementos.",
                "Comunicar interrupções via prontuário com horário, motivo, responsável e plano de retorno incluindo metas reajustadas.",
            ]
        ),
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Paciente 70 kg, alvo 30 kcal/kg/dia. Qual meta calórica diária?",
        options=("1500 kcal", "1800 kcal", "2100 kcal", "2400 kcal", "2700 kcal"),
        correct_index=2,
        difficulty="básico",
        explanation="30 kcal/kg × 70 kg = 2100 kcal por dia.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual meta proteica diária para paciente de 80 kg com queimaduras extensas (1,8 g/kg)?",
        options=("96 g", "120 g", "144 g", "180 g", "200 g"),
        correct_index=2,
        difficulty="básico",
        explanation="1,8 g/kg × 80 kg = 144 g de proteína ao dia.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual limiar de resíduo gástrico sugere necessidade de intervenção segundo diretrizes ASPEN/ESPEN?",
        options=(">150 mL", ">250 mL", ">500 mL", ">700 mL", ">1000 mL"),
        correct_index=2,
        difficulty="intermediário",
        explanation="Resíduos > 500 mL de forma repetida requerem avaliação e ajuste da terapia enteral.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual suplemento é indicado em grandes queimados para imunonutrição?",
        options=("Glutamina", "Vitamina K", "Cálcio", "Bicarbonato", "Vitamina D"),
        correct_index=0,
        difficulty="intermediário",
        explanation="Glutamina enteral (0,3 g/kg/dia) é recomendada para suporte imunológico em queimados graves.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual alvo glicêmico recomendado em pacientes críticos recebendo nutrição enteral?",
        options=("80-110 mg/dL", "110-140 mg/dL", "140-180 mg/dL", "180-220 mg/dL", ">220 mg/dL"),
        correct_index=2,
        difficulty="avançado",
        explanation="Diretrizes sugerem manter glicemia entre 140-180 mg/dL em pacientes críticos.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual abordagem reduz risco de aspiração durante infusão enteral?",
        options=("Cabeceira a 15°", "Infusão em bolus", "Posicionamento a 30-45°", "Suspender pró-cinéticos", "Reduzir hidratação"),
        correct_index=2,
        difficulty="difícil",
        explanation="Manter cabeceira elevada 30-45° reduz refluxo e aspiração.",
    ),
    MultipleChoiceQuestion(
        prompt="Paciente em vasopressor moderado (noradrenalina 0,1 mcg/kg/min) e dieta enteral. Conduta?",
        options=("Suspender dieta", "Manter dieta com monitorização", "Aumentar rapidamente velocidade", "Trocar para nutrição parenteral", "Adicionar lipídios IV"),
        correct_index=1,
        difficulty="difícil",
        explanation="Com vasopressor estável, pode-se manter enteral com vigilância de perfusão intestinal e resíduos.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual parâmetro confirma adequação proteica ao final da semana?",
        options=("Queda do peso", "Aumento da creatinina", "Balanço nitrogenado próximo de zero", "Pré-albumina em queda", "PCR elevada"),
        correct_index=2,
        difficulty="extremo",
        explanation="Balanço nitrogenado próximo de zero indica oferta proteica adequada frente ao catabolismo.",
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement="Escalas NUTRIC ajudam a definir prioridade da terapia nutricional.",
        is_true=True,
        rationale="NUTRIC estratifica risco e orienta início precoce e metas agressivas.",
    ),
    VFStatement(
        statement="Resíduos gástricos devem ser mensurados apenas uma vez ao dia.",
        is_true=False,
        rationale="Nas primeiras 48-72h recomenda-se avaliar a cada 4-6h em pacientes de alto risco.",
    ),
    VFStatement(
        statement="Vasopressores são contraindicação absoluta à nutrição enteral.",
        is_true=False,
        rationale="Doses baixas a moderadas permitem enteral com monitorização da perfusão.",
    ),
    VFStatement(
        statement="Fibra solúvel pode ajudar no manejo de diarreia.",
        is_true=True,
        rationale="Fibra solúvel melhora consistência fecal e microbiota.",
    ),
    VFStatement(
        statement="Rotina de interrupções prolongadas (>2h) deve ser evitada.",
        is_true=True,
        rationale="Interrupções prolongadas atrasam metas calóricas; planejar procedimentos para minimizar pausas.",
    ),
    VFStatement(
        statement="Nutrição enteral deve ser suspensa definitivamente diante do primeiro episódio de diarreia.",
        is_true=False,
        rationale="Investigar causas e ajustar fórmula; manter suporte sempre que possível.",
    ),
    VFStatement(
        statement="Cálcio sérico é o principal marcador de tolerância enteral.",
        is_true=False,
        rationale="Tolerância é avaliada por resíduos, distensão, evacuações e sinais de aspiração.",
    ),
    VFStatement(
        statement="Pré-albumina isoladamente não deve guiar decisão diária.",
        is_true=True,
        rationale="É influenciada por inflamação; interpretar com outros indicadores.",
    ),
    VFStatement(
        statement="Nutrição enteral precoce (<24h) reduz infecção em queimados.",
        is_true=True,
        rationale="Evidências apontam menor translocação bacteriana e complicações infecciosas.",
    ),
    VFStatement(
        statement="Sonda pós-pilórica elimina risco de aspiração.",
        is_true=False,
        rationale="Reduz risco mas não elimina; manter elevação de cabeceira e vigilância.",
    ),
    VFStatement(
        statement="Suplementação de zinco é desnecessária em grandes queimados.",
        is_true=False,
        rationale="Zinco é fundamental para cicatrização e imunidade; deve ser suplementado.",
    ),
    VFStatement(
        statement="Controle glicêmico com insulina IV pode ser necessário para atingir metas.",
        is_true=True,
        rationale="Infusões contínuas oferecem melhor ajuste em pacientes críticos com dieta enteral.",
    ),
    VFStatement(
        statement="Documentar motivo das interrupções é opcional.",
        is_true=False,
        rationale="Rastreabilidade exige registro detalhado para auditoria e melhoria de processos.",
    ),
    VFStatement(
        statement="Ferramentas digitais de prescrição ajudam a reduzir erros de volume.",
        is_true=True,
        rationale="Softwares com alarmes e cálculo automático diminuem divergências entre prescrito e infundido.",
    ),
    VFStatement(
        statement="Nutrição enteral deve ser conduzida apenas pela equipe de nutrição.",
        is_true=False,
        rationale="É responsabilidade compartilhada entre médicos, nutrição, enfermagem e fisioterapia.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 10 — Nutrição Enteral ===")
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
