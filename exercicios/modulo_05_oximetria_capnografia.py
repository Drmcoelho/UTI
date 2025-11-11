"""Quiz interativo e banco de questões do módulo 05 (oximetria e capnografia)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem='Configuração de monitores de oximetria em pacientes críticos',
        subquestions=('Quais parâmetros precisam ser configurados ao iniciar monitorização de SpO₂?', 'Como escolher local de sensor considerando perfusão periférica?', 'Quais estratégias minimizam alarmes falsos sem comprometer segurança?'),
        guidance='Definir alarmes de SpO₂ (alta 98-100%, baixa 92-94% ou personalizadas), ativar índice de perfusão e curva de pletismografia. Selecionar dedos aquecidos, lóbulo da orelha ou frente plantar conforme perfusão; aquecer membros e remover esmalte. Utilizar alarmes escalonados, delays curtos (10-15 s) e revisão diária das metas conforme perfil respiratório.',
    ),
    EssayPrompt(
        stem='Integração da capnografia ao manejo ventilatório',
        subquestions=('Como posicionar sensores mainstream versus sidestream?', 'Quais ajustes devem ser realizados ao detectar diferença elevada entre ETCO₂ e PaCO₂?', 'Quando a capnografia auxilia no diagnóstico de eventos críticos?'),
        guidance='Mainstream entre tubo e circuito; sidestream próximo à via aérea com linha seca e filtros. Diferença ETCO₂-PaCO₂ > 10 mmHg requer investigar espaço morto, débito cardíaco e calibrar ventilador. Capnografia identifica desconexão, PCR, hipoventilação e retorno espontâneo de circulação.',
    ),
    EssayPrompt(
        stem='Análise avançada da curva capnográfica',
        subquestions=('Como interpretar as fases I-IV da curva?', 'Quais padrões caracterizam broncoespasmo e reinalação?', 'Que parâmetros adicionais devem ser registrados no prontuário?'),
        guidance="Fase I (inspiração), II (mistura), III (platô alveolar), IV (inspiração). Broncoespasmo gera subida em 'tubarão', reinalação evidencia platô elevado sem retorno à linha de base. Registrar ETCO₂, forma da curva, gradiente com PaCO₂, intervenções realizadas e resposta observada.",
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt='Qual diferença máxima aceitável entre ETCO₂ e PaCO₂ em ventilação mecânica estável?',
        options=('2 mmHg', '5 mmHg', '10 mmHg', '15 mmHg', '20 mmHg'),
        correct_index=2,
        difficulty='básico',
        explanation='Diferença até 10 mmHg é esperada; valores maiores sugerem aumento do espaço morto ou hipoperfusão pulmonar.',
    ),
    MultipleChoiceQuestion(
        prompt='Platô capnográfico ascendente em dente de tubarão indica',
        options=('Circuito desconectado', 'Broncoespasmo', 'Hiperventilação', 'Reinalação de CO₂', 'Fuga no cuff'),
        correct_index=1,
        difficulty='básico',
        explanation='Formato em dente de tubarão é típico de broncoespasmo, sugerindo aumento da resistência expiratória.',
    ),
    MultipleChoiceQuestion(
        prompt='Índice de perfusão (PI) persistentemente < 0,5% sinaliza',
        options=('Perfusão periférica adequada', 'Artefato de movimento', 'Hipoperfusão periférica grave', 'Falha do oxímetro', 'Hipervolemia'),
        correct_index=2,
        difficulty='intermediário',
        explanation='PI muito baixo indica fluxo capilar insuficiente; deve-se otimizar perfusão e considerar outro sítio para o sensor.',
    ),
    MultipleChoiceQuestion(
        prompt='Queda súbita para zero na curva de ETCO₂ durante ventilação mecânica indica',
        options=('Reinalação', 'Hipotermia', 'Fuga no cuff', 'Desconexão ou parada circulatória', 'Hiperventilação'),
        correct_index=3,
        difficulty='intermediário',
        explanation='Redução abrupta sugere desconexão, obstrução severa ou PCR; verificar ventilador e checar pulso imediatamente.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual medida reduz interferência de CO na leitura da SpO₂?',
        options=('Usar sensor de dedo pediátrico', 'Aplicar sensor em região com maior melanina', 'Utilizar oxímetro com tecnologia multiwavelength', 'Aumentar tempo de integração do sinal', 'Ajustar alarme de SpO₂ para 85%'),
        correct_index=2,
        difficulty='avançado',
        explanation='Oxímetros com múltiplos comprimentos de onda diferenciam carboxihemoglobina da oxihemoglobina, aumentando acurácia.',
    ),
    MultipleChoiceQuestion(
        prompt='ETCO₂ crescendo progressivamente durante RCP indica',
        options=('Ventilação excessiva', 'Compressões eficazes e possível ROSC', 'Hipotermia', 'Desconexão do sensor', 'Erro de calibração'),
        correct_index=1,
        difficulty='avançado',
        explanation='Aumento do ETCO₂ durante RCP sugere melhora no fluxo sanguíneo e pode preceder retorno da circulação espontânea.',
    ),
    MultipleChoiceQuestion(
        prompt='SpO₂ 88% com curva pletismográfica irregular e PI 0,4% significa',
        options=('Leitura fidedigna; iniciar O₂ suplementar', 'Artefato por baixa perfusão', 'Falha de calibragem do monitor', 'Hiperventilação', 'Erro de posicionamento arterial'),
        correct_index=1,
        difficulty='difícil',
        explanation='PI baixo e curva irregular sugerem artefato; otimizar perfusão e reposicionar sensor antes de intervir agressivamente.',
    ),
    MultipleChoiceQuestion(
        prompt='Curva de ETCO₂ com retorno incompleto à linha de base sugere',
        options=('Reinalação de CO₂', 'Hiperventilação', 'Hipotermia', 'Ventilação unipulmonar', 'Obstrução da cânula nasal'),
        correct_index=0,
        difficulty='extremo',
        explanation='Retorno incompleto indica retenção de CO₂ por problemas de circuito ou absorvedor; revisar filtros e válvulas expiratórias.',
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement='A SpO₂ pode superestimar a saturação arterial em presença de carboxihemoglobina.',
        is_true=True,
        rationale='Carboxihemoglobina é interpretada como oxihemoglobina pela maioria dos oxímetros convencionais.',
    ),
    VFStatement(
        statement='O valor de ETCO₂ cai rapidamente na embolia pulmonar maciça.',
        is_true=True,
        rationale='Aumento do espaço morto reduz CO₂ exalado, gerando queda abrupta do ETCO₂.',
    ),
    VFStatement(
        statement='Capnografia sidestream retira grande volume de gás e pode causar hipoventilação.',
        is_true=False,
        rationale='Taxas de amostragem são baixas e não provocam hipoventilação clinicamente significativa.',
    ),
    VFStatement(
        statement='Perfusão periférica preservada garante leitura acurada mesmo com tremores.',
        is_true=False,
        rationale='Movimento causa artefato apesar da boa perfusão; estabilizar o membro é necessário.',
    ),
    VFStatement(
        statement='Capnografia auxilia na confirmação do posicionamento da cânula orotraqueal.',
        is_true=True,
        rationale='Presença contínua de CO₂ exalado confirma posicionamento traqueal adequado.',
    ),
    VFStatement(
        statement='Índice de perfusão é calculado dividindo a componente pulsátil pela componente estática do sinal.',
        is_true=True,
        rationale='PI = AC/DC e reflete a amplitude do pulso arterial em relação ao tecido.',
    ),
    VFStatement(
        statement='Temperaturas baixas reduzem a afinidade da hemoglobina pelo oxigênio e elevam a SpO₂.',
        is_true=False,
        rationale='Hipotermia desloca curva para a esquerda (aumenta afinidade), mas pode reduzir perfusão periférica e piorar leitura.',
    ),
    VFStatement(
        statement="Capnograma em forma de 'platô rebaixado' pode indicar ventilação unipulmonar.",
        is_true=True,
        rationale='Ventilação de um pulmão reduz o volume exalado e altera a fase III, produzindo platô oblíquo baixo.',
    ),
    VFStatement(
        statement='Monitorização contínua de ETCO₂ é recomendada durante sedação procedural profunda.',
        is_true=True,
        rationale='Capnografia detecta hipoventilação antes de quedas de SpO₂ durante sedação.',
    ),
    VFStatement(
        statement='SpO₂ de 100% exclui hipoxemia em todos os cenários.',
        is_true=False,
        rationale='Em intoxicação por CO ou metemoglobinemia, SpO₂ pode permanecer alta apesar de hipoxemia tecidual.',
    ),
    VFStatement(
        statement='Diferença ETCO₂-PaCO₂ aumenta em pacientes com choque hipovolêmico.',
        is_true=True,
        rationale='Hipoperfusão aumenta espaço morto fisiológico, ampliando gradiente entre ETCO₂ e PaCO₂.',
    ),
    VFStatement(
        statement='Capnografia nasal não é útil em pacientes em ventilação não invasiva.',
        is_true=False,
        rationale='Interfaces específicas permitem monitorar ETCO₂ e detectar hipoventilação durante VNI.',
    ),
    VFStatement(
        statement='Sinais de reinalação incluem aumento do CO₂ inspiratório (fase I).',
        is_true=True,
        rationale='Quando há reinalação, a fase inspiratória não retorna a zero e o CO₂ inspirado aumenta.',
    ),
    VFStatement(
        statement='Oxímetros devem ser calibrados manualmente a cada plantão.',
        is_true=False,
        rationale='Dispositivos modernos não exigem calibração manual, apenas testes de funcionalidade periódicos.',
    ),
    VFStatement(
        statement='A monitorização combinada de SpO₂, PI e ETCO₂ fornece panorama da oxigenação, perfusão e ventilação.',
        is_true=True,
        rationale='Integração dos indicadores permite intervenções precoces baseadas em fisiologia.',
    ),
)

def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 05 — Oximetria e Capnografia ===")
    print("Questões de múltipla escolha")
    run_mcq_session(MCQ_QUESTIONS)
    print("\nAfirmativas verdadeiro/falso")
    run_vf_session(VF_STATEMENTS)

if __name__ == "__main__":
    executar_interativo()

__all__ = ["ESSAY_PROMPTS", "MCQ_QUESTIONS", "VF_STATEMENTS", "resumo_banco", "executar_interativo"]
