"""Quiz interativo do módulo 15 (delirium em UTI)."""
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
        stem="Rastreamento estruturado de delirium",
        subquestions=(
            "Como executar CAM-ICU e ICDSC passo a passo?",
            "Quais fatores predisponentes e precipitantes devem ser registrados?",
            "Como configurar documentação eletrônica com alertas automáticos?",
        ),
        guidance="\n".join(
            [
                "CAM-ICU: avaliar RASS, realizar teste de atenção (letra A), investigar pensamento desorganizado e alteração de consciência.",
                "Registrar fatores como privação de sono, hipoxia, drogas sedativas, dor, infecção e desequilíbrios metabólicos.",
                "Criar campos obrigatórios no prontuário com alarmes para reavaliação em 12h e notificações à equipe.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Intervenções multimodais",
        subquestions=(
            "Quais componentes do bundle ABCDEF aplicar em delirium hiperativo e hipoativo?",
            "Como integrar mobilização precoce, higiene do sono e suporte familiar?",
            "Quais critérios farmacológicos para uso de dexmedetomidina, haloperidol e quetiapina?",
        ),
        guidance="\n".join(
            [
                "Aplicar bundle completo: avaliar dor, despertar diário, escolha de sedativos, prevenção de delirium, mobilização e engajamento familiar.",
                "Implementar quiet time, iluminação circadiana, exercícios com fisioterapia e visitas familiares estruturadas.",
                "Utilizar dexmedetomidina para sedação leve, haloperidol quando QTc < 500 ms e quetiapina para manutenção, sempre monitorando efeitos.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Indicadores e sustentabilidade",
        subquestions=(
            "Quais indicadores coletar (dias livres de delirium, contenções, tempo de ventilação)?",
            "Como compartilhar resultados e conduzir ciclos PDSA?",
            "Como envolver familiares em programas de reorientação cognitiva?",
        ),
        guidance="\n".join(
            [
                "Monitorar % CAM-ICU documentados 2x/dia, dias livres de delirium, uso de contenção e readmissões.",
                "Apresentar dashboards mensais, promover reuniões multiprofissionais e definir planos de ação.",
                "Treinar familiares para reorientação, uso de objetos pessoais e comunicação estruturada.",
            ]
        ),
    ),
)


MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Periodicidade recomendada do CAM-ICU?",
        options=("Semanal", "Apenas admissão", "Duas vezes ao dia", "Após extubação", "Quando família solicitar"),
        correct_index=2,
        difficulty="básico",
        explanation="Avaliação 2x/dia detecta delirium precocemente e orienta intervenções.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual fator de risco modificável prioritário?",
        options=("Idade", "Demência", "Privação de sono por ruído", "AVC prévio", "Histórico psiquiátrico"),
        correct_index=2,
        difficulty="básico",
        explanation="Controle ambiental e higiene do sono são alvos de intervenção imediata.",
    ),
    MultipleChoiceQuestion(
        prompt="Delirium hipoativo caracteriza-se por?",
        options=(
            "Agitação intensa",
            "Isolamento sensorial necessário",
            "Letargia e hipoatividade frequentemente subdiagnosticadas",
            "Ausência de risco",
            "Indicação absoluta de benzodiazepínicos",
        ),
        correct_index=2,
        difficulty="intermediário",
        explanation="Delirium hipoativo é comum e exige intervenção ativa.",
    ),
    MultipleChoiceQuestion(
        prompt="Uso de antipsicóticos deve ser?",
        options=(
            "Sempre contraindicado",
            "Realizado sem intervenção não farmacológica",
            "Associado a medidas ambientais e monitorização de QTc",
            "Mantido indefinidamente após alta",
            "Substituído por benzodiazepínicos",
        ),
        correct_index=2,
        difficulty="intermediário",
        explanation="Farmacoterapia deve ser combinada com intervenções não farmacológicas e monitorização de QTc.",
    ),
    MultipleChoiceQuestion(
        prompt="Engajamento familiar proporciona?",
        options=(
            "Nenhum impacto",
            "Aumento de ansiedade",
            "Reorientação cognitiva e redução de ansiedade",
            "Substituição da equipe",
            "Evita necessidade de mobilização",
        ),
        correct_index=2,
        difficulty="avançado",
        explanation="Família auxilia reorientação, conforto e adesão ao plano terapêutico.",
    ),
    MultipleChoiceQuestion(
        prompt="Bundle ABCDEF inclui?",
        options=(
            "Apenas ventilação",
            "Mobilização precoce e engajamento familiar",
            "Suspensão de higiene do sono",
            "Remoção de controle de dor",
            "Uso exclusivo de sedativos",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Bundle engloba dor, despertar diário, escolha de sedativos, prevenção de delirium, mobilização e família.",
    ),
    MultipleChoiceQuestion(
        prompt="Indicador essencial de qualidade?",
        options=(
            "Número de visitas",
            "Percentual de CAM-ICU documentados 2x/dia",
            "Quantidade de sedativos",
            "Dias sem fisioterapia",
            "Refeições servidas",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Documentação sistemática do CAM-ICU permite rastreabilidade e auditoria.",
    ),
    MultipleChoiceQuestion(
        prompt="Critério farmacológico chave?",
        options=(
            "QTc > 500 ms contraindica haloperidol",
            "Dexmedetomidina deve ser evitada sempre",
            "Benzodiazepínicos são primeira linha",
            "Melatonina não tem papel",
            "Antipsicóticos devem ser mantidos indefinidamente",
        ),
        correct_index=0,
        difficulty="extremo",
        explanation="QTc prolongado aumenta risco arrítmico; haloperidol deve ser evitado nesse cenário.",
    ),
)


VF_STATEMENTS = (
    VFStatement(
        statement="Delirium aumenta mortalidade e tempo de internação.",
        is_true=True,
        rationale="Estudos mostram associação com piores desfechos clínicos.",
    ),
    VFStatement(
        statement="CAM-ICU negativo exclui delirium definitivamente.",
        is_true=False,
        rationale="Avaliações seriadas e uso de outras escalas são necessários.",
    ),
    VFStatement(
        statement="Delirium hipoativo é menos perigoso que hiperativo.",
        is_true=False,
        rationale="Ambos associam-se a maior mortalidade e tempo de internação.",
    ),
    VFStatement(
        statement="Melatonina auxilia na higiene do sono.",
        is_true=True,
        rationale="Adjuvante útil na restauração do ciclo sono-vigília.",
    ),
    VFStatement(
        statement="Benzodiazepínicos reduzem risco de delirium.",
        is_true=False,
        rationale="Uso prolongado aumenta risco; preferir alternativas quando possível.",
    ),
    VFStatement(
        statement="Mobilização precoce reduz incidência de delirium.",
        is_true=True,
        rationale="Evidência robusta apoia mobilização como estratégia preventiva.",
    ),
    VFStatement(
        statement="Limitar visitas familiares reduz delirium.",
        is_true=False,
        rationale="Engajamento familiar favorece reorientação e conforto.",
    ),
    VFStatement(
        statement="Dexmedetomidina pode auxiliar em delirium hiperativo refratário.",
        is_true=True,
        rationale="Sedação cooperativa com efeito antidelirium documentado.",
    ),
    VFStatement(
        statement="Documentação estruturada não influencia auditorias.",
        is_true=False,
        rationale="Registros padronizados permitem análise e melhoria contínua.",
    ),
    VFStatement(
        statement="Antipsicóticos devem ser mantidos indefinidamente após resolução do delirium.",
        is_true=False,
        rationale="Devem ser descontinuados progressivamente conforme resolução.",
    ),
    VFStatement(
        statement="Higiene do sono inclui redução de ruído e controle de iluminação.",
        is_true=True,
        rationale="Parte central dos bundles preventivos.",
    ),
    VFStatement(
        statement="Delirium ocorre apenas em pacientes ventilados.",
        is_true=False,
        rationale="Pode ocorrer em pacientes não ventilados e em enfermarias.",
    ),
    VFStatement(
        statement="Monitorização de QTc é necessária com haloperidol ou quetiapina.",
        is_true=True,
        rationale="Evita arritmias graves em pacientes críticos.",
    ),
    VFStatement(
        statement="Educação familiar não impacta delirium.",
        is_true=False,
        rationale="Programas educativos melhoram engajamento e reorientação.",
    ),
    VFStatement(
        statement="Indicadores devem ser revisados pelo menos mensalmente.",
        is_true=True,
        rationale="Revisões periódicas sustentam melhoria contínua.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}


def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 15 — Delirium em UTI ===")
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
