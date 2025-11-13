"""Quiz interativo e banco de questões do módulo 08 (acesso arterial avançado)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem="Seleção de sítio arterial alternativo",
        subquestions=(
            "Quais fatores anatômicos e hemodinâmicos devem ser avaliados?",
            "Como a presença de suporte circulatório mecânico influencia a decisão?",
            "Qual plano de contingência deve ser definido antes do procedimento?",
        ),
        guidance="\n".join(
            [
                "Avaliar calibre do vaso, colateralidade distal, testes de Allen, presença de placas, distância à pele e necessidade de mobilização.",
                "Em pacientes com balão intra-aórtico ou ECMO, preservar femoral arterial e considerar axilar/braquial contralateral.",
                "Definir materiais específicos, equipe de apoio vascular e estratégias para controle de sangramento ou conversão.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Tunelização e fixação de cateter arterial",
        subquestions=(
            "Quais benefícios e riscos da tunelização em axilar/braquial?",
            "Como garantir estabilidade e evitar kinkings?",
            "Quais cuidados de curativo e inspeção são mandatórios?",
        ),
        guidance="\n".join(
            [
                "Tunelização reduz infecção e deslocamento, porém aumenta tempo de procedimento e risco de hematoma.",
                "Estabilizar com suturas em âncora, curativo compressivo moldado e checar curvas de pressão após cada manipulação.",
                "Curativos estéreis diários nas primeiras 48h e avaliação de perfusão distal a cada turno.",
            ]
        ),
    ),
    EssayPrompt(
        stem="Gestão de complicações",
        subquestions=(
            "Como diagnosticar precocemente isquemia distal?",
            "Quais passos seguir diante de pseudoaneurisma?",
            "Quando remover cateter e migrar para sítio alternativo?",
        ),
        guidance="\n".join(
            [
                "Isquemia: monitorar cor, temperatura, oximetria digital e doppler; se sinais presentes, notificar cirurgia vascular e aliviar curativo.",
                "Pseudoaneurisma: confirmar com ultrassom, compressão dirigida ou intervenção endovascular/cirúrgica conforme tamanho.",
                "Remover se isquemia persistente, infecção ou perda de fidelidade da curva sem correção possível.",
            ]
        ),
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt="Qual teste avalia adequação de colateralidade antes da punção braquial?",
        options=("Teste de Allen reverso", "Teste de Adson", "Teste de Barany", "Teste de Romberg", "Teste de Spurling"),
        correct_index=0,
        difficulty="básico",
        explanation="O teste de Allen (e variações) avalia colateralidade radial-ulnar para garantir perfusão distal.",
    ),
    MultipleChoiceQuestion(
        prompt="Durante punção axilar guiada, qual posição do membro superior é ideal?",
        options=("Addução completa", "Abdução 30°", "Abdução 90° com rotação externa", "Flexão 120°", "Hiperextensão"),
        correct_index=2,
        difficulty="básico",
        explanation="Abdução 90° com rotação externa expõe a artéria axilar e facilita visualização ultrassonográfica.",
    ),
    MultipleChoiceQuestion(
        prompt="Curva arterial sobremortecida (overshoot) após punção braquial sugere:",
        options=("Bolhas na linha", "Cateter dobrado", "Tubulação excessivamente complacente", "Transdutor alto demais", "Infecção local"),
        correct_index=2,
        difficulty="intermediário",
        explanation="Overshoot ocorre com sistema rígido/dinâmico; revisar extensão e conexões para reduzir artefato.",
    ),
    MultipleChoiceQuestion(
        prompt="Em paciente com balão intra-aórtico, qual sítio deve ser evitado para novo acesso arterial?",
        options=("Axilar contralateral", "Femoral ipsilateral", "Radial contralateral", "Braquial ipsilateral", "Pediosa"),
        correct_index=1,
        difficulty="intermediário",
        explanation="Femoral com balão aumenta risco de trombose/hematoma; preferir axilar ou braquial contralateral.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual intervalo recomendado para checar perfusão distal após acesso axilar?",
        options=("A cada 12h", "A cada 8h", "A cada 4h", "A cada 2h nas primeiras 24h", "Somente se sintomas"),
        correct_index=3,
        difficulty="avançado",
        explanation="Monitorização intensiva nas primeiras 24h identifica precocemente isquemia ou hematoma expansivo.",
    ),
    MultipleChoiceQuestion(
        prompt="Qual material auxilia controle de sangramento em punção axilar?",
        options=("Curativo oclusivo simples", "Dispositivo hemostático radial", "Compressão manual isolada", "Selo hemostático com espuma e faixa elástica", "Gaze comum"),
        correct_index=3,
        difficulty="difícil",
        explanation="Selo hemostático específico associado a faixa elástica moldada fornece pressão uniforme em vasos profundos.",
    ),
    MultipleChoiceQuestion(
        prompt="Paciente desenvolve pseudoaneurisma pequeno em acesso braquial. Conduta inicial?",
        options=("Observação expectante", "Compressão guiada por ultrassom", "Anticoagulação plena", "Ligadura cirúrgica imediata", "Retirada do cateter sem outras medidas"),
        correct_index=1,
        difficulty="difícil",
        explanation="Pseudoaneurismas pequenos respondem a compressão dirigida; cirurgia reservada para casos refratários.",
    ),
    MultipleChoiceQuestion(
        prompt="Queda gradual da amplitude da curva arterial com PPC preservada indica:",
        options=("Trombo mural", "Obstrução parcial na extensão", "Hipotermia", "Falta de nivelamento", "Erro de calibração do monitor"),
        correct_index=1,
        difficulty="extremo",
        explanation="Obstrução parcial na linha reduz amplitude; revisar extensão, lavar sistema e considerar troca do cateter.",
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement="Artéria axilar possui fluxo colateral que reduz risco de isquemia da mão.",
        is_true=True,
        rationale="A circulação colateral via artéria ulnar profunda e toracoacromial protege a perfusão distal.",
    ),
    VFStatement(
        statement="Punção braquial dispensa teste de Allen.",
        is_true=False,
        rationale="É essencial testar colateralidade para evitar isquemia distal após punção.",
    ),
    VFStatement(
        statement="Cateter arterial axilar deve ser fixado com pontos de seda e tipoia.",
        is_true=True,
        rationale="Fixação adequada e tipoia reduzem risco de deslocamento e tração.",
    ),
    VFStatement(
        statement="Zero hidrostático deve ser realizado ao nível do átrio direito independentemente do sítio.",
        is_true=True,
        rationale="Mantém comparabilidade das leituras de PAM e PPC.",
    ),
    VFStatement(
        statement="Tunelização aumenta risco de infecção e deve ser evitada.",
        is_true=False,
        rationale="Tunelização bem executada reduz infecção e deslocamento.",
    ),
    VFStatement(
        statement="Extensões longas reduzem sobremedida da onda arterial.",
        is_true=False,
        rationale="Extensões longas aumentam amortecimento e podem distorcer a curva.",
    ),
    VFStatement(
        statement="Curativos compressivos devem ser ajustados conforme avaliação neurológica do membro.",
        is_true=True,
        rationale="Compressão excessiva compromete perfusão e função neurológica; avaliação frequente é mandatória.",
    ),
    VFStatement(
        statement="Acesso braquial é contraindicado em pacientes com fístula AV ipsilateral.",
        is_true=True,
        rationale="Risco de trombose e perda de acesso dialítico torna o sítio inviável.",
    ),
    VFStatement(
        statement="Ultrassom doppler não é necessário após o procedimento.",
        is_true=False,
        rationale="Doppler pós-procedimento detecta trombose e pseudoaneurismas precoces.",
    ),
    VFStatement(
        statement="Analgesia regional do plexo braquial pode ser útil para punções dolorosas.",
        is_true=True,
        rationale="Bloqueio reduz movimento, dor e facilita técnica em pacientes acordados.",
    ),
    VFStatement(
        statement="Acesso axilar deve ser realizado com paciente sentado.",
        is_true=False,
        rationale="Preferir decúbito dorsal com membro abduzido e suporte adequado.",
    ),
    VFStatement(
        statement="Pseudoaneurismas grandes requerem avaliação vascular imediata.",
        is_true=True,
        rationale="Lesões volumosas podem romper; cirurgia ou endovascularidade são consideradas.",
    ),
    VFStatement(
        statement="Fluxo reverso no doppler distal é sinal benigno.",
        is_true=False,
        rationale="Fluxo reverso indica comprometimento arterial significativo e requer intervenção.",
    ),
    VFStatement(
        statement="Monitorar lactato ajuda a detectar hipoperfusão sistêmica causada por acesso inadequado.",
        is_true=True,
        rationale="Elevação persistente pode sinalizar complicações hemodinâmicas relacionadas à linha arterial.",
    ),
    VFStatement(
        statement="Não é necessário documentar avaliação neurológica após punção axilar.",
        is_true=False,
        rationale="Registro seriado de sensibilidade e motricidade é essencial para detectar neuropraxia precoce.",
    ),
)


def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 08 — Acesso Arterial Avançado ===")
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
