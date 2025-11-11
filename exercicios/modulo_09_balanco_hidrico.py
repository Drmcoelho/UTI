"""Quiz interativo e banco de questões do módulo 09 (balanço hídrico)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem="Estratégias avançadas de remoção de fluido",
        subquestions=(
            "Como calcular a fração de sobrecarga hídrica e definir meta diária?",
            "Quais combinações farmacológicas compõem o diurético sequencial?",
            "Quando migrar para ultrafiltração contínua?",
        ),
        guidance="\n".join(
            [
                "Fração = balanço acumulado/peso ideal; metas geralmente 1-1,5 L/dia ajustadas à perfusão.",
                "Diurético sequencial inclui furosemida contínua, tiazídicos, acetazolamida e antagonistas de aldosterona conforme necessidade.",
                "Iniciar ultrafiltração quando sobrecarga >10%, diurese <0,5 mL/kg/h persistente ou congestão orgânica refratária.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Integração de ferramentas de monitorização",
        subquestions=(
            "Como interpretar score VEXUS em conjunto com IVC e B-lines?",
            "Quais marcadores laboratoriais monitorar durante remoção agressiva?",
            "Como apresentar dados em rounds multiprofissionais?",
        ),
        guidance="\n".join(
            [
                "VEXUS avalia fluxo hepático, portal e renal; graus elevados combinados com IVC dilatada e B-lines generalizadas indicam congestão severa.",
                "Monitorar eletrólitos, osmolaridade, lactato, função hepática e renal, além de biomarcadores cardíacos quando apropriado.",
                "Utilizar dashboards diários com gráficos de balanço, peso, ultrassom e parâmetros laboratoriais para tomada de decisão.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Governança e segurança do balanço",
        subquestions=(
            "Quais elementos compõem o checklist diário de balanço?",
            "Como documentar entradas e saídas de forma confiável?",
            "Quais gatilhos exigem revisão imediata do plano?",
        ),
        guidance="\n".join(
            [
                "Checklist: peso diário, balanço acumulado, metas 24h, sinais de hipoperfusão, monitorização hemodinâmica e alinhamento multiprofissional.",
                "Entradas/saídas registradas hora a hora com dupla checagem entre enfermagem e equipe médica; usar sistemas eletrônicos.",
                "Revisar plano se lactato sobe, PAM cai, débito urinário reduz ou ocorre alteração neurológica/hepática.",
            ]
        ),
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Paciente 70 kg com ganho de 5 L em 48h. Fração de sobrecarga?",
        options=("3%", "5%", "7%", "9%", "12%"),
        correct_index=2,
        difficulty="básico",
        explanation="Fração = 5/70 ≈ 7% — acima de 5% já impacta desfechos em críticos.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual achado no VEXUS indica congestão hepática grave?",
        options=("Fluxo portal contínuo anterógrado", "Fluxo hepático tripásico", "Fluxo portal reverso", "Fluxo renal monofásico", "IVC colabada"),
        correct_index=2,
        difficulty="básico",
        explanation="Fluxo portal reverso é marcador de congestão venosa severa e necessidade de remoção agressiva de volume.",
    ),
    MultipleChoiceQuestion(
        prompt="Durante diurético sequencial, qual eletrólito deve ser monitorado com maior frequência?",
        options=("Cálcio", "Magnésio", "Sódio", "Potássio", "Fósforo"),
        correct_index=3,
        difficulty="intermediário",
        explanation="Perdas de potássio são significativas com diuréticos; monitorização e reposição frequente são cruciais.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual critério favorece ultrafiltração contínua em vez de intermitente?",
        options=("Hipotensão instável", "Necessidade de remoção rápida", "Sódio 150 mEq/L", "Balanço negativo leve", "Diurese 1 mL/kg/h"),
        correct_index=0,
        difficulty="intermediário",
        explanation="Pacientes hemodinamicamente instáveis toleram melhor ultrafiltração contínua com taxas baixas.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual objetivo de balanço é seguro em paciente com transplante hepático recente e congestão severa?",
        options=("-3 L/dia", "-2 L/dia", "-1,5 L/dia", "Zero", "+0,5 L/dia"),
        correct_index=2,
        difficulty="avançado",
        explanation="Remoções moderadas de 1-1,5 L/dia equilibram alívio da congestão e perfusão do enxerto.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual marcador laboratorial sinaliza hipoperfusão hepática durante remoção agressiva?",
        options=("AST/ALT em queda", "Bilirrubina indireta baixa", "Lactato crescente", "Fosfatase alcalina estável", "Albumina elevada"),
        correct_index=2,
        difficulty="difícil",
        explanation="Elevação do lactato reflete hipoperfusão sistêmica; associar com transaminases para avaliação hepática.",
    ),
    MultipleChoiceQuestion(
        prompt="Paciente em ultrafiltração contínua apresenta pressão negativa elevada no circuito. Conduta?",
        options=("Aumentar taxa de ultrafiltração", "Flushing do cateter e avaliar posição", "Suspender anticoagulação", "Trocar membrana imediatamente", "Ignorar se PAM estável"),
        correct_index=1,
        difficulty="difícil",
        explanation="Pressão negativa elevada sugere obstrução do cateter; lavar e reposicionar antes de aumentar taxa.",
    ),
    MultipleChoiceQuestion(
        prompt="Queda abrupta de débito urinário e PAM durante remoção sugere:",
        options=("Resposta adequada", "Hipoperfusão iatrogênica", "Erro de registro", "Melhora cardíaca", "Hipotermia"),
        correct_index=1,
        difficulty="extremo",
        explanation="Sinais de hipoperfusão exigem redução da taxa de remoção e reavaliação hemodinâmica imediata.",
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement="Fração de sobrecarga >10% está associada a maior mortalidade.",
        is_true=True,
        rationale="Estudos demonstram correlação entre sobrecarga elevada e piores desfechos em UTI.",
    ),
    VFStatement(
        statement="Peso diário é dispensável quando há ultrassom.",
        is_true=False,
        rationale="Peso fornece dado objetivo adicional e deve ser monitorado diariamente.",
    ),
    VFStatement(
        statement="Bioimpedância ajuda a estimar excesso de fluido intravascular.",
        is_true=True,
        rationale="Método quantifica fluido total e intravascular, guiando metas de remoção.",
    ),
    VFStatement(
        statement="IVC colabada sugere sobrecarga hídrica.",
        is_true=False,
        rationale="IVC colabada indica hipovolemia; sobrecarga cursa com IVC dilatada e pouco colabável.",
    ),
    VFStatement(
        statement="Ultrafiltração intermitente é sempre superior à contínua.",
        is_true=False,
        rationale="Escolha depende da estabilidade hemodinâmica e objetivos clínicos.",
    ),
    VFStatement(
        statement="Controle de sódio é irrelevante durante remoção agressiva.",
        is_true=False,
        rationale="Alterações rápidas de sódio podem causar complicações neurológicas; monitorização é essencial.",
    ),
    VFStatement(
        statement="Balanço positivo crônico aumenta tempo de ventilação mecânica.",
        is_true=True,
        rationale="Sobrecarga hídrica contribui para edema pulmonar e atraso no desmame.",
    ),
    VFStatement(
        statement="Score VEXUS avalia apenas veia cava inferior.",
        is_true=False,
        rationale="Inclui doppler hepático, portal e intrarrenal para graduar congestão venosa.",
    ),
    VFStatement(
        statement="Metas de balanço devem ser alinhadas com nefrologia diariamente.",
        is_true=True,
        rationale="Coordenação multiprofissional garante segurança e efetividade.",
    ),
    VFStatement(
        statement="Lactato normal garante ausência de hipoperfusão.",
        is_true=False,
        rationale="Lactato normal não exclui hipoperfusão; correlacionar com outros parâmetros.",
    ),
    VFStatement(
        statement="Diurético sequencial pode causar alcalose metabólica.",
        is_true=True,
        rationale="Uso combinado pode aumentar perdas de cloro e hidrogênio, levando à alcalose.",
    ),
    VFStatement(
        statement="Checklist diário deve incluir plano de reposição eletrolítica.",
        is_true=True,
        rationale="Reposições planejadas evitam arritmias e distúrbios eletrolíticos durante remoção.",
    ),
    VFStatement(
        statement="Ultrafiltração deve ser mantida mesmo com hipotensão persistente.",
        is_true=False,
        rationale="Hipotensão requer ajuste imediato da taxa e avaliação da necessidade de vasopressores ou pausa.",
    ),
    VFStatement(
        statement="Ganhos de peso rápidos indicam sobrecarga mesmo sem edema visível.",
        is_true=True,
        rationale="Variações >1 kg/dia sugerem acúmulo de fluido clínico relevante.",
    ),
    VFStatement(
        statement="Anotações eletrônicas são suficientes; não é preciso validação da enfermagem.",
        is_true=False,
        rationale="Dupla checagem entre equipe médica e enfermagem reduz erros de registro.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 09 — Balanço Hídrico ===")
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
