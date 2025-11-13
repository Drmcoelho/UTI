"""Quiz interativo e banco de questões do módulo 02 (monitorização não invasiva)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem='Construção de plano de trending hemodinâmico não invasivo',
        subquestions=('Quais parâmetros devem ser coletados em série para detecção precoce de deterioração?', 'Como padronizar intervalos de medida e alarmes entre equipe médica e de enfermagem?', 'Quais critérios indicam conversão para monitorização invasiva?'),
        guidance='Monitorar PAM oscilométrica, FC, índice de perfusão, temperatura periférica e lactato capilar quando disponível. Definir janelas de aferição a cada 15 minutos em instabilidade ou 1 hora em estabilidade, com alarmes de PAM < 65 mmHg e variações > 10 mmHg. Converter para invasiva diante de instabilidade refratária, divergência persistente com dados clínicos, necessidade de vasopressores em titulação rápida ou coleta gasométrica frequente.',
    ),
    EssayPrompt(
        stem='Integração da ecocardiografia point-of-care ao monitoramento não invasivo',
        subquestions=('Como selecionar janelas ecocardiográficas prioritárias para avaliação rápida?', 'Quais medidas permitem estimar débito cardíaco sem cateter invasivo?', 'Como relatar achados críticos de forma estruturada no prontuário?'),
        guidance='Priorizar eixo paraesternal longo, apical 4 câmaras e subxifoide, avaliando contratilidade global, variação do TSV e colapso de IVC. Estimar débito cardíaco via área do TSV x VTI x FC e integrar com sinais clínicos. Relatar VTI, IVC, presença de derrames e função ventricular com plano de reavaliação em 6-8h.',
    ),
    EssayPrompt(
        stem='Segurança e confiabilidade dos dispositivos não invasivos',
        subquestions=('Quais fatores interferem na leitura de SpO₂ e índice de perfusão?', 'Como validar equipamentos novos antes da adoção ampla na UTI?', 'Que estratégias mitigam alarmes falsos e fadiga de alarmes?'),
        guidance='Hipotermia, vasoconstrição periférica, pigmentação, esmalte e movimentos artefatuam leituras; aquecer extremidades e reposicionar sensor. Validar equipamentos comparando 10 leituras com padrão ouro e aplicando testes de drift. Configurar alarmes escalonados, utilizar delays inteligentes e revisão diária dos parâmetros para evitar dessensibilização.',
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt='Qual variação máxima aceitável entre três leituras consecutivas de PAM em equipamentos oscilométricos calibrados?',
        options=('2 mmHg', '5 mmHg', '8 mmHg', '12 mmHg', '15 mmHg'),
        correct_index=1,
        difficulty='básico',
        explanation='Diferenças acima de 5 mmHg indicam necessidade de repetir medida, reposicionar manguito ou validar com método invasivo.',
    ),
    MultipleChoiceQuestion(
        prompt='Para garantir leituras acuradas, o manguito deve cobrir qual percentual da circunferência do braço?',
        options=('30-40%', '40-50%', '60-80%', '90-100%', '100-120%'),
        correct_index=2,
        difficulty='básico',
        explanation='Manguitos cobrindo 60-80% da circunferência garantem transmissão adequada da pressão; tamanhos menores superestimam valores.',
    ),
    MultipleChoiceQuestion(
        prompt='Índice de perfusão < 0,7% sugere',
        options=('Boa perfusão periférica', 'Artefato sem relevância clínica', 'Hipoperfusão periférica significativa', 'Erro de leitura por excesso de luz', 'Sedação profunda suficiente'),
        correct_index=2,
        difficulty='intermediário',
        explanation='Valores < 1% apontam hipoperfusão; buscar causas como vasoconstrição, baixo débito ou hipotermia.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual combinação ecocardiográfica permite estimar volume sistólico sem acesso invasivo?',
        options=('Diâmetro telediastólico do VE e fração de ejeção', 'Área da válvula tricúspide e gradiente de pressão', 'Área do TSV e VTI do TSV', 'Volume do átrio esquerdo e pressão venosa central', 'Diâmetro da IVC e saturação venosa central'),
        correct_index=2,
        difficulty='intermediário',
        explanation='O volume sistólico é obtido multiplicando a área do TSV pelo VTI; multiplicar pelo FC gera o débito cardíaco.',
    ),
    MultipleChoiceQuestion(
        prompt='Paciente em VNI apresenta discrepância de 15 mmHg entre PAM oscilométrica e sinais clínicos. Próxima etapa?',
        options=('Assumir leitura e intensificar vasopressor', 'Solicitar gasometria arterial', 'Reposicionar manguito e repetir após 5 minutos', 'Suspender VNI', 'Iniciar ECMO'),
        correct_index=2,
        difficulty='avançado',
        explanation='Discrepância alta requer checar técnica: posicionar manguito corretamente, remover roupas apertadas e repetir medida antes de intervir.',
    ),
    MultipleChoiceQuestion(
        prompt='Durante monitorização contínua com finger-cuff, queda abrupta do sinal ocorre ao movimentar o braço. Conduta?',
        options=('Aplicar garrote proximal', 'Ajustar altura do membro ao nível do coração', 'Iniciar vasodilatador', 'Substituir sensor por pulseira pediátrica', 'Desligar alarmes para evitar ruído'),
        correct_index=1,
        difficulty='avançado',
        explanation='Variações hidrostáticas ocorrem com diferença de altura; manter membro ao nível do coração estabiliza leituras.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual fator mais impacta a confiabilidade da oximetria em pacientes com choque séptico frio?',
        options=('Uso de antibioticoterapia', 'Vasoconstrição periférica intensa', 'Administração de corticoide', 'Ventilação mecânica', 'Terapia renal substitutiva'),
        correct_index=1,
        difficulty='difícil',
        explanation='Vasoconstrição reduz fluxo capilar e amplitude do sinal, exigindo aquecimento do membro ou troca de sítio (lóbulo da orelha).',
    ),
    MultipleChoiceQuestion(
        prompt='Qual condição exige escalonamento para linha arterial?',
        options=('Paciente estável com PAM 72 mmHg', 'Uso de noradrenalina 0,05 mcg/kg/min sem variações', 'Divergência recorrente > 10 mmHg e necessidade de titulação rápida de vasopressor', 'Capnografia final baixa', 'Paciente agitado durante a aferição'),
        correct_index=2,
        difficulty='extremo',
        explanation='Divergência repetida e necessidade de ajustes finos de vasopressor são critérios clássicos para transição à monitorização invasiva.',
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement='Manguito posicionado acima do nível do coração tende a superestimar a pressão arterial.',
        is_true=False,
        rationale='Manguito alto subestima a pressão; se estiver abaixo, ocorre superestimação.',
    ),
    VFStatement(
        statement='Aferições em membros inferiores são aceitáveis quando o membro superior não está acessível.',
        is_true=True,
        rationale='É possível, porém deve-se ajustar interpretação devido a valores ligeiramente maiores na perna.',
    ),
    VFStatement(
        statement='Oximetria com índice de perfusão > 4% sugere boa perfusão periférica.',
        is_true=True,
        rationale='Valores elevados indicam fluxo capilar adequado, fortalecendo confiança na leitura de SpO₂.',
    ),
    VFStatement(
        statement='Uso de esmalte escuro altera significativamente a saturação medida.',
        is_true=True,
        rationale='Pigmentos escuros absorvem luz e podem subestimar a SpO₂; recomenda-se remover esmalte.',
    ),
    VFStatement(
        statement='Diminuição do VTI após manobra de elevação de pernas indica responsividade a fluidos.',
        is_true=False,
        rationale='Aumento do VTI sugere responsividade; queda pode indicar sobrecarga ou disfunção sistólica.',
    ),
    VFStatement(
        statement='Sensores descartáveis tipo adesivo devem ser trocados a cada 24h.',
        is_true=True,
        rationale='Trocas diárias evitam maceração cutânea e perda de aderência que gera artefato.',
    ),
    VFStatement(
        statement='SpO₂ 92% com gradiente alveolo-arterial normal dispensa investigação adicional.',
        is_true=True,
        rationale='Se gradiente é adequado e paciente estável, manter observação e correção de fatores reversíveis.',
    ),
    VFStatement(
        statement='Capnografia em circuito fechado não agrega valor à monitorização não invasiva.',
        is_true=False,
        rationale='Capnografia auxilia na avaliação de ventilação, perfusão e detecção precoce de deterioração.',
    ),
    VFStatement(
        statement='Ajustar alarmes de PAM para 50-55 mmHg em choque reduz fadiga de alarmes.',
        is_true=False,
        rationale='Alarmes muito baixos atrasam intervenção e aumentam risco de hipoperfusão irreversível.',
    ),
    VFStatement(
        statement='Monitorização contínua com finger-cuff permite detectar hipotensão ortostática durante mobilização.',
        is_true=True,
        rationale='Trending beat-to-beat evidencia quedas rápidas de PAM durante mobilização precoce.',
    ),
    VFStatement(
        statement='Ecocardiografia point-of-care substitui necessidade de avaliação cardiológica formal.',
        is_true=False,
        rationale='O POCUS complementa avaliação, mas não substitui estudo completo quando indicado.',
    ),
    VFStatement(
        statement='Variações respiratórias da IVC podem orientar reposição volêmica mesmo sem linha arterial.',
        is_true=True,
        rationale='Colapso > 50% em ventilação espontânea sugere hipovolemia significativa.',
    ),
    VFStatement(
        statement='Manguitos reutilizáveis devem ser desinfectados apenas quando visivelmente sujos.',
        is_true=False,
        rationale='Recomenda-se limpeza entre pacientes para reduzir infecção cruzada.',
    ),
    VFStatement(
        statement='Índice de perfusão pode prever sucesso de desmame de vasopressores.',
        is_true=True,
        rationale='Tendência ascendente indica melhora de perfusão periférica e tolerância à redução de drogas.',
    ),
    VFStatement(
        statement='Oscilometria é inútil em fibrilação atrial.',
        is_true=False,
        rationale='Embora haja variabilidade, medir múltiplas vezes e calcular média fornece estimativa confiável.',
    ),
)

def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 02 — Monitorização Hemodinâmica Não Invasiva ===")
    print("Questões de múltipla escolha")
    run_mcq_session(MCQ_QUESTIONS)
    print("\nAfirmativas verdadeiro/falso")
    run_vf_session(VF_STATEMENTS)

if __name__ == "__main__":
    executar_interativo()

__all__ = ["ESSAY_PROMPTS", "MCQ_QUESTIONS", "VF_STATEMENTS", "resumo_banco", "executar_interativo"]
