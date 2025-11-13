"""Quiz interativo do módulo 13 (sedação, analgesia e conforto)."""
from __future__ import annotations

from exercicios.quiz_base import (
    EssayPrompt,
    MultipleChoiceQuestion,
    VFStatement,
    run_mcq_session,
    run_vf_session,
)


ESSAY_PROMPTS = (
    EssayPrompt(
        stem="Construção de plano multimodal de sedoanalgesia",
        subquestions=(
            "Como selecionar sedativos, analgésicos e adjuvantes considerando hemodinâmica e objetivos ventilatórios?",
            "Quais metas RASS e CPOT definir para ventilação protetora?",
            "Como integrar técnicas regionais e intervenções não farmacológicas?",
        ),
        guidance="\n".join(
            [
                "Escolher agentes conforme estabilidade (dexmedetomidina em pacientes cooperativos, propofol com monitorização de PA, quetamina quando hipotensão limita opioides).",
                "Definir RASS −2 a 0 e CPOT < 3, com reavaliações frequentes.",
                "Considerar bloqueios regionais, fisioterapia, musicoterapia e comunicação familiar estruturada.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Interrupção diária e prevenção de delirium",
        subquestions=(
            "Quais critérios avaliar antes de suspender sedação?",
            "Como aplicar CAM-ICU e tratar delirium hipo vs hiperativo?",
            "Qual papel da família e da mobilização precoce nesse processo?",
        ),
        guidance="\n".join(
            [
                "Verificar estabilidade hemodinâmica, oxigenação e controle de dor antes do despertar.",
                "Aplicar CAM-ICU após despertar, tratar delirium hiperativo com dexmedetomidina/haloperidol e hipoativo com estímulo cognitivo.",
                "Engajar família e fisioterapia na reorientação, mobilização e higiene do sono.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Monitorização avançada e indicadores de desempenho",
        subquestions=(
            "Como correlacionar BIS/EEG processado com escalas clínicas?",
            "Quais indicadores acompanhar (sedação profunda não planejada, incidência de delirium, tempo até mobilização)?",
            "Como estruturar revisão mensal multiprofissional com ações corretivas?",
        ),
        guidance="\n".join(
            [
                "Manter BIS 40-60 para sedação profunda, >60 para sedação leve, correlacionando com RASS/CPOT.",
                "Monitorar % tempo RASS na meta, delirium, uso de bloqueio neuromuscular e tempo até mobilização.",
                "Promover reuniões com dashboards, análise de casos e planos PDSA.",
            ]
        ),
    ),
)


MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Meta RASS recomendada para paciente ventilado estável?",
        options=("+2", "0 a +1", "−2 a 0", "−5", "+3"),
        correct_index=2,
        difficulty="básico",
        explanation="Sedação leve a moderada (RASS −2 a 0) otimiza desfechos e reduz delirium.",
    ),
    MultipleChoiceQuestion(
        prompt="Triglicerídeos 480 mg/dL em uso de propofol contínuo. Conduta?",
        options=(
            "Manter propofol",
            "Aumentar propofol",
            "Trocar por dexmedetomidina/quetamina",
            "Suspender analgesia",
            "Adicionar benzodiazepínico",
        ),
        correct_index=2,
        difficulty="básico",
        explanation="Hipertrigliceridemia significativa exige reduzir ou trocar propofol por alternativas.",
    ),
    MultipleChoiceQuestion(
        prompt="Analgesia multimodal inclui?",
        options=(
            "Somente opioides",
            "Paracetamol, cetamina, bloqueios regionais e técnicas não farmacológicas",
            "Benzodiazepínicos isolados",
            "Apenas anti-inflamatórios",
            "Suspender sedação",
        ),
        correct_index=1,
        difficulty="intermediário",
        explanation="Associação de mecanismos reduz opioides e melhora controle de dor.",
    ),
    MultipleChoiceQuestion(
        prompt="Interrupção diária deve ocorrer quando?",
        options=(
            "Sempre que houver noradrenalina",
            "Após avaliação de estabilidade hemodinâmica e oxigenação",
            "Apenas após extubação",
            "Sem comunicação com fisioterapia",
            "Somente em pacientes cirúrgicos",
        ),
        correct_index=1,
        difficulty="intermediário",
        explanation="É necessário garantir estabilidade e envolver equipe multiprofissional.",
    ),
    MultipleChoiceQuestion(
        prompt="Delirium hiperativo deve ser manejado com?",
        options=(
            "Benzodiazepínicos indiscriminados",
            "Ambiente calmo, reorientação e haloperidol/dexmedetomidina",
            "Restrições físicas prolongadas",
            "Suspensão de analgesia",
            "Alta imediata",
        ),
        correct_index=1,
        difficulty="avançado",
        explanation="Controle ambiental e farmacológico direcionado reduzem riscos.",
    ),
    MultipleChoiceQuestion(
        prompt="Dexmedetomidina oferece?",
        options=(
            "Sedação cooperativa com menor depressão respiratória",
            "Hipertensão severa universal",
            "Contraindicação absoluta em sepse",
            "Ausência de efeito sobre delirium",
            "Impossibilidade de mobilização",
        ),
        correct_index=0,
        difficulty="difícil",
        explanation="Dexmedetomidina favorece sedação responsiva e menor delirium.",
    ),
    MultipleChoiceQuestion(
        prompt="Escala CPOT avalia?",
        options=(
            "Apenas nível de sedação",
            "Expressões faciais, movimentos e tensão muscular",
            "Somente pacientes sem tubo",
            "Sinais vitais isolados",
            "Conforto respiratório",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="CPOT utiliza indicadores comportamentais para mensurar dor em pacientes críticos.",
    ),
    MultipleChoiceQuestion(
        prompt="Bundle ABCDEF inclui?",
        options=(
            "Apenas ventilação",
            "Avaliação de dor, despertar diário, mobilização e envolvimento familiar",
            "Suspensão de mobilização",
            "Abandono da sedação",
            "Aplicação apenas em pós-operatório",
        ),
        correct_index=1,
        difficulty="extremo",
        explanation="Bundle ABCDEF estrutura cuidados integrados para reduzir delirium e melhorar desfechos.",
    ),
)


VF_STATEMENTS = (
    VFStatement(
        statement="Dexmedetomidina reduz incidência de delirium em comparação a benzodiazepínicos.",
        is_true=True,
        rationale="Estudos demonstram menor delirium com sedação alfa-2 agonista.",
    ),
    VFStatement(
        statement="Propofol em altas doses pode causar síndrome de infusão com acidose.",
        is_true=True,
        rationale="Monitorar lactato, CPK e triglicerídeos para detectar precocemente.",
    ),
    VFStatement(
        statement="Analgesia adequada contribui para menor tempo de ventilação mecânica.",
        is_true=True,
        rationale="Controle de dor melhora sincronia ventilatória e cooperação.",
    ),
    VFStatement(
        statement="Benzodiazepínicos são primeira linha para delirium hipoativo.",
        is_true=False,
        rationale="Preferir mobilização, reorientação e antipsicóticos atípicos quando necessário.",
    ),
    VFStatement(
        statement="BIS < 40 indica sedação profunda.",
        is_true=True,
        rationale="Valores baixos refletem hipnose profunda e risco de sobre sedação.",
    ),
    VFStatement(
        statement="Interrupção diária da sedação reduz tempo de UTI.",
        is_true=True,
        rationale="Despertar diário acelera extubação e reabilitação.",
    ),
    VFStatement(
        statement="CPOT > 3 sugere dor inadequadamente controlada.",
        is_true=True,
        rationale="Escala orienta ajuste de analgesia multimodal.",
    ),
    VFStatement(
        statement="Proteção ocular é desnecessária durante bloqueio neuromuscular.",
        is_true=False,
        rationale="Lubrificação e oclusão evitam abrasões corneanas.",
    ),
    VFStatement(
        statement="Quetamina pode ser adjuvante útil em pacientes hemodinamicamente instáveis.",
        is_true=True,
        rationale="Oferece analgesia e suporte hemodinâmico moderado.",
    ),
    VFStatement(
        statement="Delirium hiperativo deve ser tratado com restrição física prolongada.",
        is_true=False,
        rationale="Restrições mínimas e temporárias; priorizar controle farmacológico e ambiental.",
    ),
    VFStatement(
        statement="Mobilização precoce integra o bundle ABCDEF.",
        is_true=True,
        rationale="Elemento 'E' reforça fisioterapia e reabilitação precoce.",
    ),
    VFStatement(
        statement="Uso prolongado de opioides não gera tolerância.",
        is_true=False,
        rationale="Tolerância é comum e exige rotação e desmame estruturado.",
    ),
    VFStatement(
        statement="Intervenções musicais podem reduzir ansiedade e necessidade de sedação.",
        is_true=True,
        rationale="Evidências apoiam estratégias não farmacológicas para conforto.",
    ),
    VFStatement(
        statement="RASS deve ser registrado apenas uma vez por turno.",
        is_true=False,
        rationale="Recomenda-se monitorar frequentemente, sobretudo após ajustes de sedação.",
    ),
    VFStatement(
        statement="Sedação profunda contínua reduz risco de delirium.",
        is_true=False,
        rationale="Sedação profunda prolongada aumenta risco de delirium e complicações.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}


def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 13 — Sedação e Analgesia ===")
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
