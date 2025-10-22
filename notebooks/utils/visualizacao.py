"""Funções de visualização para parâmetros clínicos."""
import matplotlib.pyplot as plt
import numpy as np


def visualizar_parametros_ventilatorios(pbw, vc_alvo, pplat, peep, driving_pressure):
    """
    Cria visualização gráfica dos parâmetros ventilatórios.
    
    Gera dois gráficos lado a lado:
    1. Volume Corrente - mostra faixa aceitável (4-8 mL/kg) com destaque para o alvo (6 mL/kg)
    2. Pressões Ventilatórias - mostra PEEP, Pressão de Platô e Driving Pressure com limites recomendados
    
    Parâmetros:
    -----------
    pbw : float
        Peso Predito (PBW) em kg
    vc_alvo : float
        Volume corrente alvo em mL (6 mL/kg)
    pplat : float
        Pressão de platô em cmH2O
    peep : float
        PEEP em cmH2O
    driving_pressure : float
        Driving pressure (ΔP) em cmH2O
    """
    # Calcular valores de volume corrente
    vc_min = pbw * 4
    vc_max = pbw * 8
    
    # Criar figura com dois subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfico 1: Volume Corrente
    categories = ['Mínimo\n(4 mL/kg)', 'ALVO\n(6 mL/kg)', 'Máximo\n(8 mL/kg)']
    values = [vc_min, vc_alvo, vc_max]
    colors = ['#ffd93d', '#6bcf7f', '#ffd93d']
    
    bars1 = ax1.bar(categories, values, color=colors, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Volume (mL)', fontsize=12, fontweight='bold')
    ax1.set_title('Volume Corrente - Ventilação Protetora', fontsize=13, fontweight='bold')
    ax1.axhline(y=vc_alvo, color='red', linestyle='--', linewidth=2, alpha=0.7)
    
    # Adicionar valores nas barras
    for bar, value in zip(bars1, values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.0f} mL',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Gráfico 2: Pressões
    pressure_labels = ['PEEP', 'Pplat', 'ΔP']
    pressure_values = [peep, pplat, driving_pressure]
    pressure_limits = [5, 30, 15]  # Limites recomendados
    
    x_pos = np.arange(len(pressure_labels))
    bars2 = ax2.bar(x_pos, pressure_values, color=['#4ecdc4', '#ff6b6b', '#ffd93d'],
                    edgecolor='black', linewidth=2, label='Valor Atual')
    
    # Adicionar linhas de limite
    for i, (val, lim) in enumerate(zip(pressure_values, pressure_limits)):
        if i == 0:  # PEEP (mínimo)
            ax2.axhline(y=lim, color='green', linestyle='--', linewidth=1.5, alpha=0.5)
        else:  # Pplat e ΔP (máximo)
            ax2.axhline(y=lim, color='red', linestyle='--', linewidth=1.5, alpha=0.5)
    
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(pressure_labels)
    ax2.set_ylabel('Pressão (cmH2O)', fontsize=12, fontweight='bold')
    ax2.set_title('Pressões Ventilatórias', fontsize=13, fontweight='bold')
    
    # Adicionar valores nas barras
    for bar, value in zip(bars2, pressure_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    plt.show()
