"""Quiz interativo do módulo 14 (bloqueio neuromuscular em UTI)."""
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
        stem="Indicação e titulação do bloqueio neuromuscular",
        subquestions=(
            "Quais critérios clínicos justificam bloqueio contínuo em SDRA grave?",
            "Como ajustar infusão guiada por TOF e contagem postetânica?",
            "Quais metas adotar para evitar bloqueio profundo prolongado?",
        ),
        guidance="\n".join(
            [
                "Indicar quando PaO₂/FiO₂ < 150 com ventilação protetora, assincronias graves ou hipertensão intracraniana refratária.",
                "Ajustar infusão visando TOF 1-2/4 e contagem postetânica 1-3, reavaliando a cada 30-60 minutos inicialmente.",
                "Documentar metas claras, revisar diariamente e reduzir dose ao menor nível efetivo.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Bundles de segurança durante bloqueio",
        subquestions=(
            "Quais cuidados oculares, cutâneos e musculoesqueléticos implementar?",
            "Como integrar fisioterapia e enfermagem na mobilização passiva?",
            "Como estruturar checklist de documentação multiprofissional?",
        ),
        guidance="\n".join(
            [
                "Lubrificar olhos, realizar oclusão, mudar decúbito a cada 2h, usar colchões de alívio e monitorizar pele.",
                "Fisioterapia deve conduzir mobilização passiva, exercícios respiratórios e alongamentos diários.",
                "Checklist compartilhado com horário de intervenções, responsáveis e sinais de complicações.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Desmame, reversão e reabilitação",
        subquestions=(
            "Quais critérios definem início do desmame?",
            "Como conduzir testes de suspensão e avaliar sincronização ventilatória?",
            "Quais estratégias de reabilitação iniciar após suspensão?",
        ),
        guidance="\n".join(
            [
                "Iniciar desmame quando melhora oxigenação (PaO₂/FiO₂ > 150), estabilidade hemodinâmica e ausência de assincronias graves.",
                "Suspender infusão por 30-60 min, avaliar TOF, padrões ventilatórios e necessidade de ajuste sedativo.",
                "Implementar fisioterapia ativa, avaliação neurológica seriada e plano de reabilitação precoce.",
            ]
        ),
    ),
)


MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Meta de TOF durante bloqueio contínuo para SDRA grave?",
        options=("0/4", "1-2/4", "3-4/4", "4/4", "Não monitorar"),
        correct_index=1,
        difficulty="básico",
        explanation="Alvo 1-2 respostas mantém sincronia ventilatória sem bloqueio profundo excessivo.",
    ),
    MultipleChoiceQuestion(
        prompt="Contagem postetânica ausente (0) sugere?",
        options=(
            "Bloqueio superficial",
            "Bloqueio profundo que exige redução",
            "Avaliação inadequada",
            "Ausência de efeito do fármaco",
            "Necessidade de aumentar dose",
        ),
        correct_index=1,
        difficulty="intermediário",
        explanation="Contagem zero indica bloqueio profundo, devendo reduzir infusão se clinicamente possível.",
    ),
    MultipleChoiceQuestion(
        prompt="Medida essencial de proteção ocular?",
        options=(
            "Compressas frias apenas",
            "Lubrificação frequente e oclusão",
            "Antibiótico tópico diário",
            "Nenhuma ação necessária",
            "Uso de lentes rígidas",
        ),
        correct_index=1,
        difficulty="intermediário",
        explanation="Lubrificar e ocluir olhos previne abrasões corneanas durante bloqueio.",
    ),
    MultipleChoiceQuestion(
        prompt="Bradicardia associada ao bloqueio contínuo deve levar a?",
        options=(
            "Suspender definitivamente",
            "Avaliar sedativos e ajustar doses",
            "Iniciar beta-bloqueador",
            "Ignorar se assintomática",
            "Aumentar infusão",
        ),
        correct_index=1,
        difficulty="avançado",
        explanation="Revisar sedação e titulação do bloqueador, tratando causas associadas antes de suspender.",
    ),
    MultipleChoiceQuestion(
        prompt="Neuropatia do doente crítico relaciona-se principalmente a?",
        options=(
            "Uso de vitaminas",
            "Imobilidade, sepse e hiperglicemia",
            "Bloqueio neuromuscular isolado",
            "Ventilação mecânica",
            "Uso de anticoagulantes",
        ),
        correct_index=1,
        difficulty="avançado",
        explanation="Fatores sistêmicos e imobilidade prolongada aumentam risco de neuropatia.",
    ),
    MultipleChoiceQuestion(
        prompt="Estratégia segura de desmame?",
        options=(
            "Suspensão abrupta",
            "Redução gradual com reavaliação do TOF",
            "Aumento de sedação compensatória",
            "Desconsiderar assincronias",
            "Aguardar extubação",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Redução progressiva com monitorização evita assincronias e recaídas.",
    ),
    MultipleChoiceQuestion(
        prompt="Uso de nervo facial para TOF é útil quando?",
        options=(
            "Paciente sem edema",
            "Edema periférico limita avaliação ulnar",
            "Sempre contraindicado",
            "Apenas em sedação leve",
            "Incompatível com rocurônio",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Nervo facial auxilia monitorização quando membros superiores não respondem adequadamente.",
    ),
    MultipleChoiceQuestion(
        prompt="Contraindicação relativa ao bloqueio prolongado?",
        options=(
            "Hipoxemia grave",
            "Falta de monitorização objetiva",
            "Ventilação controlada",
            "Uso de dexmedetomidina",
            "Traqueostomia",
        ),
        correct_index=1,
        difficulty="extremo",
        explanation="Sem TOF monitorado aumenta risco de bloqueio excessivo e complicações.",
    ),
)


VF_STATEMENTS = (
    VFStatement(
        statement="TOF 0/4 garante bloqueio adequado e seguro.",
        is_true=False,
        rationale="TOF zero pode indicar bloqueio profundo excessivo; utilize contagem postetânica.",
    ),
    VFStatement(
        statement="Bloqueio prolongado aumenta risco de neuropatia do doente crítico.",
        is_true=True,
        rationale="Imobilidade e drogas contribuem para fraqueza neuromuscular.",
    ),
    VFStatement(
        statement="Lubrificação ocular deve ocorrer pelo menos a cada 4h.",
        is_true=True,
        rationale="Reduz abrasões e ressecamento corneano.",
    ),
    VFStatement(
        statement="Sedação profunda torna desnecessária a monitorização do TOF.",
        is_true=False,
        rationale="Sedação não substitui monitorização neuromuscular objetiva.",
    ),
    VFStatement(
        statement="Mobilização passiva deve continuar mesmo sob bloqueio.",
        is_true=True,
        rationale="Previne contraturas e preserva perfusão.",
    ),
    VFStatement(
        statement="Contagem postetânica > 5 sugere bloqueio superficial.",
        is_true=True,
        rationale="Valores altos indicam retorno da transmissão neuromuscular.",
    ),
    VFStatement(
        statement="Bloqueadores neuromusculares não alteram frequência cardíaca.",
        is_true=False,
        rationale="Alguns agentes podem induzir bradicardia ou hipotensão.",
    ),
    VFStatement(
        statement="Sugamadex reverte bloqueio por rocurônio em situações de necessidade.",
        is_true=True,
        rationale="Permite reversão rápida de bloqueio profundo não planejado.",
    ),
    VFStatement(
        statement="Desmame do bloqueio deve ser realizado somente pelo médico.",
        is_true=False,
        rationale="Protocolos multiprofissionais permitem atuação coordenada.",
    ),
    VFStatement(
        statement="Elevação isolada de CK obriga suspensão imediata do bloqueio.",
        is_true=False,
        rationale="Interpretar no contexto clínico antes de decidir pela suspensão.",
    ),
    VFStatement(
        statement="Bloqueio facilita sincronização ventilatória na SDRA grave.",
        is_true=True,
        rationale="Reduz assincronias e melhora oxigenação em fases agudas.",
    ),
    VFStatement(
        statement="Analgesia pode ser suspensa quando paciente está bloqueado.",
        is_true=False,
        rationale="Analgesia deve ser mantida para prevenir sofrimento e instabilidade autonômica.",
    ),
    VFStatement(
        statement="Checklists diários aumentam adesão às medidas de segurança.",
        is_true=True,
        rationale="Documentação estruturada garante rastreabilidade e accountability.",
    ),
    VFStatement(
        statement="Ausência de TOF no nervo facial garante bloqueio diafragmático.",
        is_true=False,
        rationale="Pode haver discrepância; correlacionar com parâmetros ventilatórios.",
    ),
    VFStatement(
        statement="Pronação prolongada exige vigilância adicional de pontos de pressão.",
        is_true=True,
        rationale="Risco elevado de lesões de pele durante pronas prolongadas.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}


def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 14 — Bloqueio Neuromuscular ===")
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
