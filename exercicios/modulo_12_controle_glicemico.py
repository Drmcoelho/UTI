"""Quiz interativo do módulo 12 (controle glicêmico em pacientes críticos)."""
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
        stem="Protocolos baseados em taxa de variação glicêmica",
        subquestions=(
            "Como calcular a taxa de variação e ajustar a infusão para meta 110-160 mg/dL?",
            "Quais adaptações aplicar em pacientes sob NPT contínua e corticoterapia?",
            "Como garantir registro estruturado e checagem dupla em cada ajuste?",
        ),
        guidance="\n".join(
            [
                "Calcular delta glicêmico/tempo e aplicar protocolo dinâmico para aumentar ou reduzir infusão.",
                "Reduzir fator de sensibilidade em NPT/corticoide, intensificar monitorização horária e considerar insulina adicionada à NPT.",
                "Registrar em prontuário eletrônico, validar com dupla checagem de enfermagem e incluir justificativa clínica.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Prevenção e manejo de hipoglicemia",
        subquestions=(
            "Quais gatilhos reconhecer (pausa de dieta, erro de bomba, insuficiência renal)?",
            "Como estruturar algoritmo de resgate e reavaliação pós-evento?",
            "Quais indicadores acompanhar para melhoria contínua?",
        ),
        guidance="\n".join(
            [
                "Mapear interrupções de dieta, falhas de bomba, clearance renal reduzido e uso de betabloqueadores.",
                "Administrar dextrose IV, reavaliar em 10-15 min, ajustar infusão e documentar evento crítico.",
                "Monitorar % glicemias < 70 mg/dL, tempo para correção e reincidências, discutindo em reuniões de segurança.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Auditoria e integração multiprofissional",
        subquestions=(
            "Como calcular tempo na meta (Time in Range) e variabilidade glicêmica?",
            "Quais estratégias de feedback e educação contínua implementar?",
            "Como correlacionar indicadores com protocolos de nutrição e sedação?",
        ),
        guidance="\n".join(
            [
                "Time in Range = medições na meta / total; variabilidade pelo desvio padrão ou coeficiente de variação.",
                "Promover dashboards semanais, reuniões interdisciplinares e treinamentos focados em lacunas.",
                "Cruzar dados com mudanças de dieta, sedativos e status de infecção para intervenções conjuntas.",
            ]
        ),
    ),
)


MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Qual faixa glicêmica alvo recomendada para a maioria dos pacientes críticos?",
        options=(
            "80-110 mg/dL",
            "90-120 mg/dL",
            "110-140 mg/dL",
            "140-180 mg/dL",
            "180-220 mg/dL",
        ),
        correct_index=3,
        difficulty="básico",
        explanation="Diretrizes recomendam 140-180 mg/dL como alvo seguro para pacientes críticos.",
    ),
    MultipleChoiceQuestion(
        prompt="Taxa de variação +40 mg/dL/h sugere?",
        options=(
            "Reduzir infusão",
            "Manter infusão",
            "Aumentar infusão conforme protocolo",
            "Suspender monitorização",
            "Iniciar bolo de insulina",
        ),
        correct_index=2,
        difficulty="básico",
        explanation="Elevações rápidas exigem intensificação segundo escalas dinâmicas.",
    ),
    MultipleChoiceQuestion(
        prompt="Interrupção de dieta por 60 min requer?",
        options=(
            "Manter infusão igual",
            "Administrar bolo de insulina",
            "Reduzir 50% ou suspender temporariamente",
            "Aumentar alvo para 250 mg/dL",
            "Nenhuma ação",
        ),
        correct_index=2,
        difficulty="intermediário",
        explanation="Pausas de dieta demandam redução proporcional ou suspensão da infusão de insulina.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual fórmula auxilia a estimar fator de sensibilidade à insulina em regime basal-bolus?",
        options=(
            "Regra 1500",
            "Regra 1800",
            "Regra 500",
            "Regra 100",
            "Não existe",
        ),
        correct_index=1,
        difficulty="intermediário",
        explanation="Regra 1800 (1800/dose total diária) adapta queda esperada por unidade de insulina.",
    ),
    MultipleChoiceQuestion(
        prompt="Indicador prioritário de qualidade no controle glicêmico?",
        options=(
            "Número de seringas utilizadas",
            "Tempo na meta glicêmica",
            "Volume de soro glicosado",
            "Total de refeições",
            "Tempo de internação",
        ),
        correct_index=1,
        difficulty="avançado",
        explanation="Time in Range correlaciona-se com desfechos clínicos e deve ser monitorado.",
    ),
    MultipleChoiceQuestion(
        prompt="Hipoglicemia grave (< 40 mg/dL) exige?",
        options=(
            "Nenhum registro",
            "Notificação e análise de segurança",
            "Suspender insulina definitivamente",
            "Ignorar se assintomática",
            "Aumentar dextrose sem monitorar",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Eventos graves devem ser registrados, analisados e gerar planos corretivos.",
    ),
    MultipleChoiceQuestion(
        prompt="Dexmedetomidina pode?",
        options=(
            "Dispensar monitorização",
            "Mascarar sinais autonômicos de hipoglicemia",
            "Reduzir necessidade de dupla checagem",
            "Eliminar protocolo de insulina",
            "Curar diabetes",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Sedação com dexmedetomidina pode mascarar sinais clínicos, exigindo vigilância intensificada.",
    ),
    MultipleChoiceQuestion(
        prompt="Integração com NPT requer atenção principalmente a?",
        options=(
            "Lipídios",
            "Dextrose",
            "Vitaminas",
            "Água livre",
            "Sódio",
        ),
        correct_index=1,
        difficulty="extremo",
        explanation="A velocidade de dextrose define carga glicêmica e necessidade de insulina adicional.",
    ),
)


VF_STATEMENTS = (
    VFStatement(
        statement="Protocolos de insulina IV devem incluir checagem dupla em cada ajuste.",
        is_true=True,
        rationale="Dupla checagem reduz erros de medicação em ambiente crítico.",
    ),
    VFStatement(
        statement="Meta 80-110 mg/dL é recomendada rotineiramente em todos os pacientes críticos.",
        is_true=False,
        rationale="Alvos muito baixos aumentam risco de hipoglicemia e mortalidade.",
    ),
    VFStatement(
        statement="Variabilidade glicêmica elevada correlaciona-se com maior mortalidade.",
        is_true=True,
        rationale="Oscilações amplas estão associadas a piores desfechos clínicos.",
    ),
    VFStatement(
        statement="Corticoterapia reduz necessidade de insulina.",
        is_true=False,
        rationale="Corticoides aumentam resistência à insulina e demandam maior vigilância.",
    ),
    VFStatement(
        statement="Tempo na meta é calculado dividindo medições dentro do alvo pelo total.",
        is_true=True,
        rationale="Métrica simples e padronizada para auditoria.",
    ),
    VFStatement(
        statement="Pausas de dieta não influenciam risco de hipoglicemia.",
        is_true=False,
        rationale="Interrupções sem ajuste elevam risco de hipoglicemia grave.",
    ),
    VFStatement(
        statement="Ajustes na NPT não impactam o controle glicêmico.",
        is_true=False,
        rationale="Alterações calóricas mudam demanda de insulina.",
    ),
    VFStatement(
        statement="Hipoglicemia deve ser comunicada à equipe multiprofissional.",
        is_true=True,
        rationale="Permite investigação de causa e ações corretivas conjuntas.",
    ),
    VFStatement(
        statement="Dexmedetomidina não interfere na percepção de hipoglicemia.",
        is_true=False,
        rationale="Sedativos podem mascarar sinais autonômicos de hipoglicemia.",
    ),
    VFStatement(
        statement="Monitorização arterial contínua dispensa glicemia capilar.",
        is_true=False,
        rationale="É necessário correlacionar leituras e calibrar periodicamente.",
    ),
    VFStatement(
        statement="Pacientes em TSR contínua requerem ajustes específicos de insulina.",
        is_true=True,
        rationale="Mudanças no clearance e nas soluções infundidas alteram demanda de insulina.",
    ),
    VFStatement(
        statement="Registrar apenas hipoglicemias sintomáticas é suficiente.",
        is_true=False,
        rationale="Eventos assintomáticos também devem ser registrados e analisados.",
    ),
    VFStatement(
        statement="Indicadores de controle glicêmico devem ser revisados mensalmente no mínimo.",
        is_true=True,
        rationale="Revisões periódicas sustentam melhoria contínua.",
    ),
    VFStatement(
        statement="Agonistas beta-2 reduzem glicemia e dispensam monitorização.",
        is_true=False,
        rationale="Podem elevar glicemia; monitorização segue necessária.",
    ),
    VFStatement(
        statement="Interrupções frequentes de dieta exigem revisão do protocolo de insulina.",
        is_true=True,
        rationale="Reajustes previnem hipoglicemias recorrentes.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}


def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 12 — Controle Glicêmico ===")
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
