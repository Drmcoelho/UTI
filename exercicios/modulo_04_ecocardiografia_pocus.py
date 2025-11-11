"""Quiz interativo e banco de questões do módulo 04 (ecocardiografia à beira do leito)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem='Execução do protocolo RUSH em pacientes instáveis',
        subquestions=('Quais janelas compõem o protocolo e que achados críticos devem ser documentados?', 'Como integrar os achados com sinais vitais e monitorização invasiva/não invasiva?', 'Quais limites definem necessidade de intervenção imediata (ex.: tamponamento)?'),
        guidance='Protocolo RUSH inclui janelas cardicas (parasternal, apical, subxifoide), pulmonares, cava inferior e vasos pélvicos. Registrar contratilidade global, derrame pericárdico, colapso de IVC, pneumotórax e tamponamento. Integrar com PAM/PPV e estado clínico; tamponamento indicado por derrame com colapso diastólico de VD e IVC tensa requer pericardiocentese.',
    ),
    EssayPrompt(
        stem='Quantificação funcional pela ecocardiografia beira-leito',
        subquestions=('Como estimar fração de ejeção rapidamente?', 'Qual abordagem para medir VTI do TSV e derivar débito cardíaco?', 'Quais parâmetros permitem distinguir choque cardiogênico de distributivo?'),
        guidance='Utilizar método eyeballing aliado ao Simpson simplificado quando possível, comparando movimento de paredes. Medir diâmetro do TSV em parasternal longo, calcular área (πr²) e multiplicar pelo VTI obtido em apical 5 câmaras; multiplicar por FC para débito. Fração de ejeção baixa com VTI reduzido e RVS elevada sugere choque cardiogênico; FE normal com VTI alto e RVS baixa indica distributivo.',
    ),
    EssayPrompt(
        stem='Governança e documentação de estudos à beira-leito',
        subquestions=('Quais elementos devem constar no laudo resumido?', 'Como arquivar loops e imagens para revisão?', 'Que plano de reavaliação deve ser pactuado com a equipe?'),
        guidance='Laudo deve conter indicação, janelas obtidas, FE estimada, VTI, IVC, presença de derrames, sinais de congestão pulmonar e recomendações. Loops armazenados no PACS ou pasta segura com identificação do paciente. Planejar reavaliação em 6-12h ou após intervenções (fluido, vasopressor) com checagem cruzada por intensivista ou cardiologista.',
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt='Qual estrutura anatômica deve ser medida para calcular a área do TSV?',
        options=('Diâmetro interno da válvula mitral', 'Diâmetro interno do trato de saída do ventrículo esquerdo', 'Espessura do septo interventricular', 'Área do átrio esquerdo', 'Circunferência da válvula tricúspide'),
        correct_index=1,
        difficulty='básico',
        explanation='O diâmetro do TSV (LVOT) em vista paraesternal longo é utilizado para calcular a área e, posteriormente, o volume sistólico.',
    ),
    MultipleChoiceQuestion(
        prompt='Durante protocolo RUSH, qual achado sugere tamponamento cardíaco?',
        options=('Hipercinesia global', 'Derrame pericárdico pequeno sem colapso', 'Colapso diastólico do ventrículo direito com IVC dilatada', 'IVC colabando > 50%', 'Padrão B lines difuso'),
        correct_index=2,
        difficulty='básico',
        explanation='Tamponamento combina derrame relevante, colapso diastólico de VD e IVC distendida sem colapso respiratório.',
    ),
    MultipleChoiceQuestion(
        prompt='Queda do VTI de 21 para 14 cm após bolus de fluidos indica',
        options=('Resposta volêmica adequada', 'Hiperdistensão ventricular', 'Erro de medição', 'Necessidade de aumentar vasodilatadores', 'Tamponamento'),
        correct_index=1,
        difficulty='intermediário',
        explanation='Redução do VTI após fluidos sugere sobrecarga ou falência ventricular; interromper fluidos e avaliar suporte inotrópico.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual valor de TAPSE indica disfunção significativa do VD?',
        options=('> 22 mm', '17-20 mm', '< 17 mm', '< 25 mm', '> 30 mm'),
        correct_index=2,
        difficulty='intermediário',
        explanation='TAPSE < 17 mm indica disfunção sistólica do ventrículo direito segundo diretrizes da ASE.',
    ),
    MultipleChoiceQuestion(
        prompt='Em choque distributivo, espera-se encontrar',
        options=('VE hiperdinâmico com VTI alto', 'VE hipodinâmico com VTI baixo', 'Derrame pericárdico volumoso', 'IVC rígida sem colapso', 'VD dilatado com septo em D'),
        correct_index=0,
        difficulty='avançado',
        explanation='Choque distributivo cursa com hiperdinamismo e VTI elevado; entretanto, avaliar resposta a fluido e tônus vascular.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual combinação indica congestão pulmonar à ultrassonografia?',
        options=('Linhas A difusas', 'Linhas B multifocais bilaterais', 'Deslizamento pleural preservado', 'Sinal do código de barras', 'Sinal do espelho'),
        correct_index=1,
        difficulty='avançado',
        explanation='Múltiplas linhas B bilaterais indicam edema intersticial; correlacionar com clínica e PEEP para manejo ventilatório.',
    ),
    MultipleChoiceQuestion(
        prompt='Ao realizar avaliação de cava inferior em ventilação mecânica controlada, colapso < 12% sugere',
        options=('Hipovolemia severa', 'Status volêmico adequado', 'Sobrecarga volêmica', 'Erro técnico', 'Tamponamento'),
        correct_index=2,
        difficulty='difícil',
        explanation='Colapso respiratório < 12% em ventilação controlada indica alta pressão de enchimento e possível sobrecarga volêmica.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual estratégia aumenta a reprodutibilidade da medida de VTI?',
        options=('Usar amostra maior no Doppler pulsado (PW)', 'Manter ângulo insonação < 20°', 'Medir apenas uma vez por exame', 'Posicionar cursor no centro do átrio esquerdo', 'Executar manobra de Valsalva'),
        correct_index=1,
        difficulty='extremo',
        explanation='Ângulo < 20° minimiza erro de coseno; também promediar 3-5 ciclos melhora consistência entre examinadores.',
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement='POCUS pode ser realizado por intensivistas treinados seguindo protocolos padronizados.',
        is_true=True,
        rationale='Diretrizes recentes reconhecem competência de intensivistas desde que submetidos a treinamento estruturado.',
    ),
    VFStatement(
        statement='Avaliação de IVC em ventilação espontânea utiliza limiar de colapso > 50% para sugerir hipovolemia.',
        is_true=True,
        rationale='Colapso acentuado sugere baixa pressão de enchimento em pacientes espontaneamente ventilando.',
    ),
    VFStatement(
        statement='Linhas A indicam edema pulmonar.',
        is_true=False,
        rationale='Linhas A representam pulmão aerado normal; edema gera linhas B.',
    ),
    VFStatement(
        statement='VTI deve ser medido em apical 4 câmaras.',
        is_true=False,
        rationale='O VTI do TSV é medido preferencialmente em apical 5 câmaras alinhando Doppler com fluxo de saída.',
    ),
    VFStatement(
        statement='TAPSE avalia a função sistólica do ventrículo direito.',
        is_true=True,
        rationale='Tricuspid Annular Plane Systolic Excursion reflete deslocamento longitudinal do VD.',
    ),
    VFStatement(
        statement='Derrame pericárdico pequeno sem colapso exige drenagem imediata.',
        is_true=False,
        rationale='Derrames pequenos sem repercussão podem ser acompanhados clinicamente.',
    ),
    VFStatement(
        statement='Protocolo BLUE diferencia causas de insuficiência respiratória aguda.',
        is_true=True,
        rationale='BLUE analisa perfis A, B, C para distinguir edema, pneumonia, pneumotórax e tromboembolismo.',
    ),
    VFStatement(
        statement='Ângulo Doppler acima de 60° mantém precisão adequada para VTI.',
        is_true=False,
        rationale='Ângulos altos superestimam VTI; recomenda-se < 20° com correção quando necessário.',
    ),
    VFStatement(
        statement='Choque obstrutivo por TEP pode mostrar VD dilatado e septo em D.',
        is_true=True,
        rationale='Sobrecarga aguda de pressão no VD causa deformidade septal característica.',
    ),
    VFStatement(
        statement='IVC com diâmetro < 1,5 cm sempre indica hipovolemia.',
        is_true=False,
        rationale='Deve-se considerar contexto clínico; pacientes com PEEP alta podem ter colapso independente de volume.',
    ),
    VFStatement(
        statement='POCUS não substitui ecocardiograma formal quando há suspeita de endocardite.',
        is_true=True,
        rationale='Casos complexos exigem estudo completo com Doppler e transesofágico se necessário.',
    ),
    VFStatement(
        statement='Sinal do pulmão seco (linhas A e deslizamento presente) descarta pneumotórax.',
        is_true=False,
        rationale='Para descartar pneumotórax é necessário visualizar o sinal do deslizamento ou linhas B; linhas A isoladas não são suficientes.',
    ),
    VFStatement(
        statement='Anotações estruturadas no laudo facilitam auditoria e treinamento.',
        is_true=True,
        rationale='Templates padronizados garantem rastreabilidade e comparabilidade entre exames.',
    ),
    VFStatement(
        statement='POCUS não deve ser repetido após intervenções para evitar fadiga da equipe.',
        is_true=False,
        rationale='Repetir após terapias permite avaliar resposta e ajustar condutas.',
    ),
    VFStatement(
        statement='Medida de strain global longitudinal é obrigatória em todos os exames beira-leito.',
        is_true=False,
        rationale='Strain é avançado e não obrigatório no POCUS inicial, embora útil quando disponível.',
    ),
)

def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 04 — Ecocardiografia à Beira do Leito (POCUS) ===")
    print("Questões de múltipla escolha")
    run_mcq_session(MCQ_QUESTIONS)
    print("\nAfirmativas verdadeiro/falso")
    run_vf_session(VF_STATEMENTS)

if __name__ == "__main__":
    executar_interativo()

__all__ = ["ESSAY_PROMPTS", "MCQ_QUESTIONS", "VF_STATEMENTS", "resumo_banco", "executar_interativo"]
