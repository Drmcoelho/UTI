"""Quiz interativo e banco de questões do módulo 01 (monitorização invasiva)."""
from __future__ import annotations

from exercicios.quiz_base import EssayPrompt, MultipleChoiceQuestion, VFStatement, run_mcq_session, run_vf_session

ESSAY_PROMPTS = (
    EssayPrompt(
        stem='Implantação de PAI em choque séptico refratário',
        subquestions=('Quais critérios clínicos reforçam a necessidade da linha arterial neste cenário?', 'Como preparar a equipe e o material para garantir assepsia e calibração adequadas?', 'Quais checkpoints imediatos devem ser documentados após a punção?'),
        guidance='Indicar PAI diante de vasopressores em escalada, necessidade de trending beat-to-beat, lactato elevado e sinais de hipoperfusão periférica. Preparar bandeja estéril, kit pressurizado purgado, checklist de barreira máxima e monitor multiparamétrico calibrado. Documentar sítio de punção, horário, pressões iniciais, teste de Allen, zero atmosférico e parâmetros de alarmes.',
    ),
    EssayPrompt(
        stem='Manutenção diária da linha arterial',
        subquestions=('Quais cuidados reduzem risco de infecção e trombose?', 'Como conduzir a troca do curativo e a avaliação do sítio?', 'Quais indicadores levam à retirada do cateter?'),
        guidance='Realizar higienização rigorosa, manter sistema pressurizado fechado, evitar desconexões e garantir purge a 3 mL/h. Curativo estéril trocado a cada 7 dias ou quando sujo/úmido, inspeção diária de hiperemia e sinais de isquemia. Retirar após estabilidade hemodinâmica, ausência de necessidade de trending contínuo, queda do risco-benefício ou sinais de infecção.',
    ),
    EssayPrompt(
        stem='Integração da monitorização invasiva com a condução da ressuscitação',
        subquestions=('Como interpretar a curva arterial amortecida versus sobremortecida?', 'Quais parâmetros derivados auxiliam na decisão de fluidos?', 'Como comunicar as metas durante rounds multiprofissionais?'),
        guidance='Amortecimento sugere bolhas, extensão excessiva ou filtro saturado; sobremortecimento (overshoot) indica tubulação complacente ou pressão dinâmica elevada. Utilizar PAM, PPV, elevação passiva de pernas e testes de oclusão de fim de expiração para orientar fluidos. Registrar metas em prontuário, alinhando PAM alvo, PPV desejada, ajustes de vasopressor e plano de reavaliação com enfermagem e fisioterapia.',
    ),
)

MCQ_QUESTIONS = (
    MultipleChoiceQuestion(
        prompt='Qual intervalo de tempo é aceitável entre a realização do zero atmosférico e a conexão do sistema ao paciente?',
        options=('Pode ultrapassar 30 minutos se o circuito permanecer fechado', 'Até 20 minutos desde que a bolsa permaneça pressurizada', 'Máximo de 5 minutos para evitar erro por temperatura e bolhas', 'Zero pode ser feito após a conexão ao paciente sem prejuízo', 'Não existe recomendação sobre o intervalo'),
        correct_index=2,
        difficulty='básico',
        explanation='Quanto maior o intervalo após o zero, maior a chance de variação térmica e formação de microbolhas; recomenda-se conectar imediatamente (até 5 minutos).',
    ),
    MultipleChoiceQuestion(
        prompt='Qual estratégia reduz sobremaneira o risco de amortecimento da curva arterial?',
        options=('Utilizar cateter de polietileno de maior calibre', 'Aumentar a altura do transdutor acima da linha axilar média', 'Adicionar filtro bacteriano próximo ao paciente', 'Manter extensão o mais curta e rígida possível', 'Injetar 5 mL de ar no flush para aumentar o tônus'),
        correct_index=3,
        difficulty='básico',
        explanation='Tubulação longa/complacente causa amortecimento; usar extensões curtas e rígidas com conexões firmes previne distorção da onda.',
    ),
    MultipleChoiceQuestion(
        prompt='Paciente com PPV 18% e pressão de pulso 30 mmHg em ventilação controlada. Qual a conduta inicial mais segura?',
        options=('Iniciar vasopressina em bolus', 'Avaliar responsividade a fluidos com elevação passiva de pernas', 'Aumentar a PEEP para 12 cmH₂O', 'Administrar 500 mL de coloide sem teste prévio', 'Iniciar nitroprussiato para reduzir pós-carga'),
        correct_index=1,
        difficulty='intermediário',
        explanation='PPV elevada sugere responsividade a fluidos; teste dinâmico como elevação passiva de pernas evita sobrecarga desnecessária.',
    ),
    MultipleChoiceQuestion(
        prompt='Ao realizar teste de flush, observa-se retorno oscilatório com mais de três ondas. O que isso indica?',
        options=('Sistema superdamping, necessitando de filtro adicional', 'Sistema underdamping com risco de superestimar PAS', 'Transdutor desalinhado abaixo da linha axilar média', 'Bolhas de ar no cateter causando artefato', 'Oclusão arterial iminente'),
        correct_index=1,
        difficulty='intermediário',
        explanation='Oscilações persistentes após o flush indicam underdamping; é necessário revisar comprimento do tubo e possíveis conexões frouxas para evitar superestimação da PAS.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual parâmetro integrado à curva arterial sugere necessidade de escalonar vasopressor mesmo com PAM 66 mmHg?',
        options=('Tempo de enchimento capilar < 2 s', 'Índice de perfusão periférica 4%', 'Lactato 5,2 mmol/L e diurese 0,2 mL/kg/h', 'Saturação venosa central 72%', 'Temperatura 37,5 ºC'),
        correct_index=2,
        difficulty='avançado',
        explanation='PAM marginal com lactato elevado e oligúria indica hipoperfusão; além de otimizar volume, considera-se escalonar vasopressor para metas ≥ 70 mmHg.',
    ),
    MultipleChoiceQuestion(
        prompt='Durante calibração, a PAM exibida cai para 40 mmHg após desconexão do transdutor da bolsa pressurizada. Qual a causa mais provável?',
        options=('Buraco no diafragma do transdutor', 'Bolha residual entre o cateter e o transdutor', 'Bag pressurizada insuficiente', 'Falha no sensor de temperatura do monitor', 'Volume de flush excessivo'),
        correct_index=2,
        difficulty='difícil',
        explanation='Quando a bolsa perde pressão (300 mmHg), ocorre refluxo de sangue e queda abrupta da leitura; re-pressurizar imediatamente evita coagulação no sistema.',
    ),
    MultipleChoiceQuestion(
        prompt='Em paciente com fibrilação atrial, como interpretar PPV de 14%?',
        options=('Valor confiável para predizer responsividade a fluidos', 'Necessidade imediata de cateter venoso central', 'Indicativo de erro de calibração', 'PPV torna-se menos confiável; combinar com ecocardiografia', 'Sinal direto para suspender vasopressores'),
        correct_index=3,
        difficulty='difícil',
        explanation='Arritmias reduzem a acurácia da PPV; é preciso correlacionar com variação de IVC ou VTI no eco para tomada de decisão.',
    ),
    MultipleChoiceQuestion(
        prompt='Qual critério abaixo sinaliza retirada segura do cateter arterial?',
        options=('Noradrenalina 0,3 mcg/kg/min com PAM 68 mmHg', 'Paciente em ventilação mecânica assisto-controlada', 'Necessidade de coletas gasométricas a cada 6 horas', 'Estabilidade hemodinâmica mantida > 24h sem ajustes', 'Planejamento de cateter venoso central'),
        correct_index=3,
        difficulty='extremo',
        explanation='Retirada ocorre quando paciente mantém metas sem ajustes, sem necessidade de trending beat-to-beat ou coletas frequentes, reduzindo risco de infecção e trombose.',
    ),
)

VF_STATEMENTS = (
    VFStatement(
        statement='O zero atmosférico deve ser feito com o transdutor aberto ao ar e nivelado na linha axilar média.',
        is_true=True,
        rationale='Zero incorreto gera erro sistemático de PAM; alinhar à linha axilar evita sub ou superestimação.',
    ),
    VFStatement(
        statement='Flush contínuo acima de 5 mL/h reduz risco de trombose sem efeitos adversos.',
        is_true=False,
        rationale='Taxas elevadas provocam sobrecarga volêmica e risco de hemodiluição; recomenda-se 2-3 mL/h.',
    ),
    VFStatement(
        statement='PPV elevada em ventilação espontânea mantém a mesma interpretação que em ventilação controlada.',
        is_true=False,
        rationale='Respiração espontânea altera ciclos pressóricos; PPV perde acurácia e deve ser evitada.',
    ),
    VFStatement(
        statement='Pressurizar a bolsa em 300 mmHg garante fluxo contínuo e previne refluxo sanguíneo.',
        is_true=True,
        rationale='300 mmHg assegura fluxo unidirecional do flush e evita coagulação na linha.',
    ),
    VFStatement(
        statement='A curva arterial sobremortecida (overshoot) tende a subestimar a PAS.',
        is_true=False,
        rationale='Overshoot superestima PAS e subestima PAD; revisar complacência do sistema.',
    ),
    VFStatement(
        statement='Monitorização radial é contraindicada em pacientes com enxerto radial recente.',
        is_true=True,
        rationale='Uso da artéria radial pode comprometer fluxo do enxerto; preferir sítio alternativo.',
    ),
    VFStatement(
        statement='Ajustar a altura do leito não altera a leitura desde que o transdutor esteja fixo no suporte.',
        is_true=False,
        rationale='Qualquer variação de altura modifica a referência hidrostática; transdutor deve acompanhar o nível do paciente.',
    ),
    VFStatement(
        statement='Curva com incisura dicrótica pouco evidente pode indicar vasoplegia severa.',
        is_true=True,
        rationale='Vasoplegia reduz resistência vascular e atenua incisura; correlacionar com quadro clínico.',
    ),
    VFStatement(
        statement='Em uso de balão intra-aórtico, a leitura da PAM é inviável.',
        is_true=False,
        rationale='Pode haver artefato, mas PAM média continua mensurável com análise da curva sincronizada.',
    ),
    VFStatement(
        statement='Cateter arterial deve ser trocado rotineiramente a cada 72h para evitar infecção.',
        is_true=False,
        rationale='Trocas programadas aumentam complicações; manter até indicação clínica ou sinais de infecção.',
    ),
    VFStatement(
        statement='Doppler transcraniano pode complementar a monitorização invasiva na avaliação de perfusão.',
        is_true=True,
        rationale='Fluxo cerebral auxilia na titulação de PAM em pacientes neurocríticos.',
    ),
    VFStatement(
        statement='Amostras para gasometria arterial devem ser coletadas lentamente para evitar colapso da linha.',
        is_true=False,
        rationale='Coletas devem ser firmes e sem refluxo prolongado para minimizar risco de coágulo.',
    ),
    VFStatement(
        statement='Em pacientes com ECMO venoarterial, a curva arterial pode não refletir perfusão coronariana.',
        is_true=True,
        rationale='Fluxo retrogrado altera forma da onda; interpretar em conjunto com eco e pós-carga.',
    ),
    VFStatement(
        statement='Temperaturas muito baixas no paciente reduzem a viscosidade e melhoram fidelidade da curva.',
        is_true=False,
        rationale='Hipotermia altera resposta do transdutor e aumenta risco de espasmo; curva pode deteriorar.',
    ),
    VFStatement(
        statement='Manter registro diário dos alarmes configurados facilita auditoria de eventos sentinela.',
        is_true=True,
        rationale='Checklist documentado assegura rastreabilidade e segurança assistencial.',
    ),
)

def resumo_banco() -> dict[str, int]:
    """Retorna contagem das questões para validação automatizada."""
    return {"dissertativas": len(ESSAY_PROMPTS), "mcq": len(MCQ_QUESTIONS), "vf": len(VF_STATEMENTS)}

def executar_interativo() -> None:
    """Executa sessão completa com MCQ e V/F no terminal."""
    print("=== Módulo 01 — Monitorização Hemodinâmica Invasiva ===")
    print("Questões de múltipla escolha")
    run_mcq_session(MCQ_QUESTIONS)
    print("\nAfirmativas verdadeiro/falso")
    run_vf_session(VF_STATEMENTS)

if __name__ == "__main__":
    executar_interativo()

__all__ = ["ESSAY_PROMPTS", "MCQ_QUESTIONS", "VF_STATEMENTS", "resumo_banco", "executar_interativo"]
