"""Quiz interativo e banco de questões do módulo 11 (nutrição parenteral total)."""
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
        stem="Prescrição completa da NPT nas primeiras 72h",
        subquestions=(
            "Como definir peso de referência e calorias alvo (proteína, carboidrato, lipídio)?",
            "Quais ajustes diários considerar para eletrólitos e controle glicêmico?",
            "Como escalonar a oferta para prevenir síndrome de realimentação?",
        ),
        guidance="\n".join(
            [
                "Utilizar peso ajustado/ideal para desnutrição, distribuir 20% proteína, 20% lipídio e 60% carboidrato com 1,5-2 g/kg de proteína.",
                "Reavaliar sódio, potássio, magnésio e fósforo a cada 12-24h, ajustar insulina e hidratação conforme glicemias.",
                "Escalonar 60→80→100% da meta conforme estabilidade de eletrólitos e suplementação de tiamina.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Gerenciamento de complicações metabólicas",
        subquestions=(
            "Como monitorar triglicerídeos, enzimas hepáticas e osmolaridade?",
            "Quais intervenções realizar diante de TG > 400 mg/dL ou elevação de transaminases?",
            "Qual plano para hiperglicemia persistente apesar da insulina basal?",
        ),
        guidance="\n".join(
            [
                "Dosar TG e função hepática 2-3x/semana, correlacionar com osmolaridade e balanço hídrico.",
                "Suspender ou reduzir lipídio 24-48h, investigar colestase, ajustar carboidratos e avaliar necessidade de emulsões alternativas.",
                "Ativar protocolo de insulina IV com metas 140-180 mg/dL, revisar taxa de dextrose e aporte calórico não proteico.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Transição e alta com nutrição parenteral",
        subquestions=(
            "Quais critérios definem possibilidade de transição para enteral parcial?",
            "Como preparar equipe e família para nutrição parenteral domiciliar?",
            "Quais indicadores acompanhar após a alta (infecção, reinternação, metas calóricas)?",
        ),
        guidance="\n".join(
            [
                "Considerar transição quando TGI funcional atinge ≥ 60% da meta calórica e não há contra-indicações mecânicas.",
                "Treinar enfermagem e cuidadores em técnica asséptica, bombas, alarmes e plano de exames periódicos.",
                "Monitorar infecção relacionada a cateter, peso, marcadores nutricionais, readmissões e adesão a consultas multiprofissionais.",
            ]
        ),
    ),
)


MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Quando a NPT exclusiva é indicada de forma imperativa?",
        options=(
            "Resíduos gástricos de 150 mL",
            "Pacientes em dieta oral pós-cirurgia bariátrica",
            "Fístula entérica de alto débito com íleo prolongado",
            "Pancreatite leve com tolerância oral",
            "Diarreia por antibiótico",
        ),
        correct_index=2,
        difficulty="básico",
        explanation="Fístulas de alto débito com íleo impedem nutrição enteral eficaz, exigindo NPT exclusiva.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual distribuição calórica clássica para NPT balanceada?",
        options=(
            "70% carboidrato, 10% proteína, 20% lipídio",
            "40% carboidrato, 40% proteína, 20% lipídio",
            "60% carboidrato, 20% proteína, 20% lipídio",
            "30% carboidrato, 30% proteína, 40% lipídio",
            "80% carboidrato, 10% proteína, 10% lipídio",
        ),
        correct_index=2,
        difficulty="básico",
        explanation="Distribuição 60/20/20 mantém balanço calórico adequado e aporte proteico suficiente.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual osmolaridade máxima aceitável para infusão periférica prolongada?",
        options=(
            "600 mOsm/L",
            "700 mOsm/L",
            "900 mOsm/L",
            "1100 mOsm/L",
            "1500 mOsm/L",
        ),
        correct_index=1,
        difficulty="intermediário",
        explanation="Acima de 700-750 mOsm/L o risco de flebite aumenta e deve-se preferir via central.",
    ),
    MultipleChoiceQuestion(
        prompt="Medida fundamental para prevenir síndrome de realimentação ao iniciar NPT?",
        options=(
            "Iniciar com 100% das calorias",
            "Suspender tiamina",
            "Suplementar fósforo, magnésio e tiamina previamente",
            "Aumentar lipídios para 50%",
            "Infundir dextrose em bolus",
        ),
        correct_index=2,
        difficulty="intermediário",
        explanation="Reposição de micronutrientes e escalonamento gradual reduzem risco de refeeding.",
    ),
    MultipleChoiceQuestion(
        prompt="Triglicerídeos chegaram a 450 mg/dL no dia 3. Conduta?",
        options=(
            "Aumentar infusão de lipídio",
            "Suspender lipídio por 24-48h",
            "Reduzir dextrose e aumentar lipídio",
            "Aumentar velocidade da bomba",
            "Adicionar bicarbonato",
        ),
        correct_index=1,
        difficulty="avançado",
        explanation="Hipertrigliceridemia significativa demanda suspensão temporária do lipídio e reintrodução gradual.",
    ),
    MultipleChoiceQuestion(
        prompt="Monitorização de eletrólitos nas primeiras 72h deve incluir?",
        options=(
            "Sódio e potássio semanais",
            "Magnésio e fósforo diários",
            "Cloro mensal",
            "Cálcio anual",
            "Bicarbonato irrelevante",
        ),
        correct_index=1,
        difficulty="difícil",
        explanation="Mg e fósforo caem rapidamente com refeeding e exigem dosagem diária no início.",
    ),
    MultipleChoiceQuestion(
        prompt="Medida essencial para prevenir infecção associada à NPT?",
        options=(
            "Trocar equipos a cada 96h",
            "Manter curativo aberto",
            "Realizar curativo estéril a cada 48h",
            "Utilizar cateter compartilhado com vasopressores",
            "Dispensar técnica asséptica",
        ),
        correct_index=2,
        difficulty="difícil",
        explanation="Curativos estéreis frequentes e uso exclusivo do cateter reduzem infecção.",
    ),
    MultipleChoiceQuestion(
        prompt="Critério chave para considerar home parenteral?",
        options=(
            "Necessidade < 500 kcal/dia",
            "Uso de acesso temporário",
            "Paciente estável com equipe treinada",
            "Ausência de suporte familiar",
            "Dispensa acompanhamento semanal",
        ),
        correct_index=2,
        difficulty="extremo",
        explanation="Home parenteral requer estabilidade clínica, suporte familiar e equipe capacitada.",
    ),
)


VF_STATEMENTS = (
    VFStatement(
        statement="NPT exclusiva é indicada quando enteral não atinge > 60% das necessidades por 7 dias em pacientes de alto risco.",
        is_true=True,
        rationale="Diretrizes sugerem NPT precoce em pacientes de alto risco nutricional sem progressão enteral adequada.",
    ),
    VFStatement(
        statement="Relação caloria não proteica/nitrogênio ideal deve ficar abaixo de 60:1.",
        is_true=False,
        rationale="O alvo clássico situa-se entre 100-120:1 para evitar sobrecarga de carboidratos.",
    ),
    VFStatement(
        statement="Tiamina deve ser administrada antes e durante os primeiros dias de NPT.",
        is_true=True,
        rationale="Reduz risco de encefalopatia e síndrome de realimentação.",
    ),
    VFStatement(
        statement="Cateter dedicado à NPT pode ser usado para coletas frequentes de sangue.",
        is_true=False,
        rationale="Uso exclusivo reduz contaminação e risco de infecção.",
    ),
    VFStatement(
        statement="Osmolaridade elevada aumenta risco de trombose venosa periférica.",
        is_true=True,
        rationale="Soluções hipertônicas em veia periférica provocam flebite e trombose.",
    ),
    VFStatement(
        statement="Lipídios devem ser infundidos rapidamente para reduzir tempo de manipulação.",
        is_true=False,
        rationale="Infusão lenta (12-24h) minimiza hiperlipidemia e eventos adversos.",
    ),
    VFStatement(
        statement="Síndrome de refeeding cursa com hipofosfatemia, hipomagnesemia e retenção hídrica.",
        is_true=True,
        rationale="Distúrbios eletrolíticos caracterizam o quadro e exigem reposição agressiva.",
    ),
    VFStatement(
        statement="Ajustes de insulina são desnecessários em pacientes em NPT.",
        is_true=False,
        rationale="Controle glicêmico rigoroso é parte do bundle de segurança em NPT.",
    ),
    VFStatement(
        statement="Micronutrientes podem ser omitidos nos primeiros dias sem prejuízo.",
        is_true=False,
        rationale="Vitaminas e oligoelementos devem ser administrados desde o início para evitar deficiências.",
    ),
    VFStatement(
        statement="Inspeção diária do sítio de cateter é componente obrigatório do bundle.",
        is_true=True,
        rationale="Avaliação visual e troca de curativo conforme protocolo reduzem infecções.",
    ),
    VFStatement(
        statement="NPT suplementar está associada a menor mortalidade em cirurgias de alto risco nutricional.",
        is_true=True,
        rationale="Evidências suportam suplementação precoce em pacientes de alto risco.",
    ),
    VFStatement(
        statement="Balanço hídrico não precisa considerar volume da NPT.",
        is_true=False,
        rationale="Volume de NPT deve integrar balanço para evitar sobrecarga ou hipovolemia.",
    ),
    VFStatement(
        statement="Hipertrigliceridemia exige suspensão temporária de lipídios.",
        is_true=True,
        rationale="Triglicerídeos > 400-500 mg/dL requerem pausa ou redução da infusão de lipídios.",
    ),
    VFStatement(
        statement="Fósforo normal no primeiro dia dispensa monitorização subsequente.",
        is_true=False,
        rationale="Níveis podem despencar após início da NPT; vigilância contínua é crítica.",
    ),
    VFStatement(
        statement="Infusão cíclica pode ser considerada para pacientes estáveis em longo prazo.",
        is_true=True,
        rationale="Permite períodos livres de infusão, melhora qualidade de vida e reduz complicações hepáticas.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}


def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 11 — Nutrição Parenteral Total ===")
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
