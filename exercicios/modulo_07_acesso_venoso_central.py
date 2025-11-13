"""Quiz interativo e banco de questões do módulo 07 (acesso venoso central)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem="Preparação e planejamento de acesso central em paciente de alto risco",
        subquestions=(
            "Quais elementos devem constar no checklist pré-procedimento?",
            "Como personalizar a escolha do sítio em obesidade mórbida e coagulopatia?",
            "Quais estratégias minimizam punções repetidas?",
        ),
        guidance="\n".join(
            [
                "Checklist inclui confirmação de indicação, consentimento, revisão de alergias, exames laboratoriais, equipamentos completos e plano de contingência.",
                "Em obesidade/coagulopatia avaliar compressibilidade, distância pele-via, preferência por jugular guiada e uso de correção parcial de coagulopatia.",
                "Minimizar punções com ultrassom em tempo real, agulha ecogênica, manobras de Valsalva e aspirar antes de dilatar.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Controle de infecção e manutenção de cateter",
        subquestions=(
            "Quais são os componentes do bundle de inserção?",
            "Como organizar rotina de curativos e locks?",
            "Como auditar indicadores de infecção relacionados a cateter?",
        ),
        guidance="\n".join(
            [
                "Bundle: barreira máxima, clorexidina alcoólica, seleção de sítio ideal, ultrassom, troca de circuitos estéreis.",
                "Curativos transparentes a cada 7 dias (ou antes), locks com solução salina/heparina ou antimicrobiana conforme risco.",
                "Auditoria inclui densidade de incidência por 1000 cateter-dia, conformidade com bundle e feedback periódico.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Manejo de complicações imediatas",
        subquestions=(
            "Qual algoritmo para punção arterial inadvertida?",
            "Como conduzir suspeita de pneumotórax pós-procedimento?",
            "Quando indicar remoção e reintrodução em novo sítio?",
        ),
        guidance="\n".join(
            [
                "Se punção arterial com cateter pequeno: retirar e compressão. Se dilatador ou cateter grande: manter, chamar cirurgia vascular.",
                "Pneumotórax: monitorização clínica, ultrassom/raio-X imediato, drenagem se sintomático ou grande.",
                "Remover e trocar de sítio em caso de múltiplas punções fracassadas, hematoma expansivo ou sinais de infecção precoce.",
            ]
        ),
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Qual fator reduz significativamente infecções em CVC?",
        options=("Uso exclusivo de luvas estéreis", "Cobertura com gaze", "Chapéu e máscara para o paciente", "Aplicação de clorexidina alcoólica 2%", "Troca diária do cateter"),
        correct_index=3,
        difficulty="básico",
        explanation="Clorexidina alcoólica 2% para antissepsia cutânea reduz colonização e infecções relacionadas a cateter.",
    ),
    MultipleChoiceQuestion(
        prompt="Ao usar ultrassom, qual estrutura anatômica deve ser identificada antes da punção da veia jugular interna?",
        options=("Válvula tricúspide", "Artéria carótida comum", "Artéria subclávia", "Veia jugular externa", "Nervo frênico"),
        correct_index=1,
        difficulty="básico",
        explanation="Identificar carótida reduz risco de punção arterial; manter agulha lateral à artéria sob visualização contínua.",
    ),
    MultipleChoiceQuestion(
        prompt="Durante punção femoral observa-se fluxo pulsátil brilhante. Conduta imediata?",
        options=("Manter fio-guia e prosseguir", "Realizar compressão e redirecionar", "Infundir solução salina", "Aspirar lentamente e confirmar saturação venosa", "Inserir dilatador rapidamente"),
        correct_index=1,
        difficulty="intermediário",
        explanation="Fluxo pulsátil indica punção arterial; retirar agulha e comprimir para evitar hematoma expansivo.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual método confirma posicionamento adequado da ponta do cateter?",
        options=("Contagem de centímetros da pele", "Ultrassom intraoperatório", "Raio-X anteroposterior com ponta no átrio direito alto", "Palpação de pulsos", "Medida de saturação venosa central"),
        correct_index=2,
        difficulty="intermediário",
        explanation="Radiografia com ponta no átrio direito alto (ou junção cava-AD) confirma posicionamento seguro.",
    ),
    MultipleChoiceQuestion(
        prompt="Em pacientes com múltiplas linhas, qual estratégia reduz trombose relacionada a cateter?",
        options=("Posicionar cateteres no mesmo vaso", "Evitar mobilização", "Usar lúmens de menor calibre possível", "Trocar cateteres a cada 3 dias", "Utilizar cateter impregnado com prata"),
        correct_index=2,
        difficulty="avançado",
        explanation="Lúmens menores e adequados ao objetivo reduzem estase e trombose, além de permitir fluxo laminar.",
    ),
    MultipleChoiceQuestion(
        prompt="Quando considerar cateter de acesso periférico central (PICC) em vez de CVC tradicional?",
        options=("Necessidade de noradrenalina alta", "Terapia de curto prazo (<48h)", "Quimioterapia prolongada e difícil acesso", "Monitorização hemodinâmica invasiva", "Hemodiálise emergencial"),
        correct_index=2,
        difficulty="difícil",
        explanation="PICC é indicado para terapias prolongadas com osmolaridade moderada; não é ideal para vasopressores em altas doses ou hemodinâmica avançada.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual abordagem reduz risco de pneumotórax na punção subclávia?",
        options=("Aspirar continuamente", "Inserir agulha com ângulo de 60°", "Utilizar ultrassom com acesso infraclavicular lateral", "Posicionar paciente com 30° de Trendelenburg reverso", "Retirar fio-guia rapidamente"),
        correct_index=2,
        difficulty="difícil",
        explanation="Ultrassom em plano infraclavicular permite visualizar pleura e guia trajetória, reduzindo risco de pneumotórax.",
    ),
    MultipleChoiceQuestion(
        prompt="Paciente com CVC apresenta hiperemia e secreção purulenta. Qual passo inicial?",
        options=("Trocar curativo e manter", "Iniciar antibiótico sistêmico sem coleta", "Retirar cateter e coletar ponta para cultura", "Aumentar fluxo de heparina", "Solicitar TC torácica"),
        correct_index=2,
        difficulty="extremo",
        explanation="Sinais claros de infecção local exigem remoção do cateter e cultura da ponta, associado a antibioticoterapia guiada.",
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement="Trendelenburg 10-15° reduz risco de embolia gasosa na punção jugular.",
        is_true=True,
        rationale="A posição aumenta pressão venosa e distende a veia, reduzindo entrada de ar.",
    ),
    VFStatement(
        statement="Uso rotineiro de cateter impregnado é obrigatório em todos os pacientes.",
        is_true=False,
        rationale="Indicados apenas em unidades com alta taxa de infecção ou pacientes de altíssimo risco.",
    ),
    VFStatement(
        statement="Tempo máximo recomendado de permanência do CVC é 48 horas.",
        is_true=False,
        rationale="Cateteres podem permanecer enquanto indicados e sem sinais de complicação; trocas programadas aumentam risco.",
    ),
    VFStatement(
        statement="Monitorização ultrassonográfica pós-procedimento identifica trombose precoce.",
        is_true=True,
        rationale="Ultrassom é sensível para trombose venosa e deve ser usado diante de suspeita clínica.",
    ),
    VFStatement(
        statement="Punção subclávia guiada por ultrassom reduz complicações em comparação à técnica landmark.",
        is_true=True,
        rationale="Estudos demonstram menor taxa de pneumotórax e punção arterial com ultrassom.",
    ),
    VFStatement(
        statement="Curativos transparentes devem ser trocados a cada 48h.",
        is_true=False,
        rationale="Recomenda-se troca a cada 7 dias ou se sujo/descolado.",
    ),
    VFStatement(
        statement="Não é necessário uso de máscara durante inserção se operador estiver vacinado.",
        is_true=False,
        rationale="Máscara faz parte da barreira máxima independente do status vacinal.",
    ),
    VFStatement(
        statement="Teste de refluxo com transdutor de pressão ajuda a confirmar posicionamento venoso.",
        is_true=True,
        rationale="Colocar transdutor mostra onda venosa e evita dilatação inadvertida de artéria.",
    ),
    VFStatement(
        statement="Cateter femoral deve ser evitado em obesidade mórbida devido a infecção.",
        is_true=False,
        rationale="Pode ser usado com técnica estéril; risco infeccioso aumenta, mas decisão depende do contexto e habilidade.",
    ),
    VFStatement(
        statement="É seguro infundir noradrenalina concentrada em cateter periférico de grosso calibre por tempo indeterminado.",
        is_true=False,
        rationale="Vasopressores devem ser preferencialmente em acesso central para reduzir risco de extravasamento e necrose.",
    ),
    VFStatement(
        statement="ECG de fio-guia pode ajudar a confirmar localização no átrio.",
        is_true=True,
        rationale="Método de posicionamento por ECG identifica contato com parede atrial e evita deslocamentos excessivos.",
    ),
    VFStatement(
        statement="Troca sobre fio é adequada mesmo em suspeita de infecção local.",
        is_true=False,
        rationale="Em suspeita de infecção, deve-se remover e inserir em novo sítio para evitar colonização cruzada.",
    ),
    VFStatement(
        statement="Pacientes em ventilação não invasiva não devem receber CVC.",
        is_true=False,
        rationale="CVC pode ser necessário; apenas ajustar suporte ventilatório e proteção de vias aéreas durante procedimento.",
    ),
    VFStatement(
        statement="Treinamento regular com simuladores está associado à redução de complicações.",
        is_true=True,
        rationale="Simulação melhora habilidades técnicas e aderência a protocolos.",
    ),
    VFStatement(
        statement="Documentar lote de materiais é opcional.",
        is_true=False,
        rationale="Rastreabilidade exige registro de lote, data e hora para investigação de eventos.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 07 — Acesso Venoso Central ===")
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
