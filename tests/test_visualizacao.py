"""Tests for the visualization module."""
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt


def test_visualizar_parametros_ventilatorios_runs():
    """Test that the visualization function runs without errors."""
    from notebooks.utils.visualizacao import visualizar_parametros_ventilatorios
    
    # Test with sample parameters
    pbw = 66.0
    vc_alvo = 396.0
    pplat = 28
    peep = 10
    driving_pressure = 18
    
    # Should not raise any exceptions
    visualizar_parametros_ventilatorios(pbw, vc_alvo, pplat, peep, driving_pressure)
    plt.close('all')  # Clean up
    

def test_visualizar_parametros_ventilatorios_creates_figure():
    """Test that the visualization function creates a figure."""
    from notebooks.utils.visualizacao import visualizar_parametros_ventilatorios
    
    # Clear any existing figures
    plt.close('all')
    
    # Test with sample parameters
    pbw = 70.0
    vc_alvo = 420.0
    pplat = 30
    peep = 12
    driving_pressure = 18
    
    visualizar_parametros_ventilatorios(pbw, vc_alvo, pplat, peep, driving_pressure)
    
    # Check that a figure was created
    assert len(plt.get_fignums()) > 0, "No figure was created"
    
    # Clean up
    plt.close('all')


def test_visualizar_parametros_ventilatorios_with_edge_cases():
    """Test the visualization function with edge case parameters."""
    from notebooks.utils.visualizacao import visualizar_parametros_ventilatorios
    
    # Test with minimum values
    visualizar_parametros_ventilatorios(
        pbw=45.0,
        vc_alvo=270.0,
        pplat=20,
        peep=5,
        driving_pressure=15
    )
    plt.close('all')
    
    # Test with maximum typical values
    visualizar_parametros_ventilatorios(
        pbw=100.0,
        vc_alvo=600.0,
        pplat=35,
        peep=20,
        driving_pressure=15
    )
    plt.close('all')


if __name__ == '__main__':
    print("Running visualization tests...")
    
    print("Test 1: Basic function execution...")
    test_visualizar_parametros_ventilatorios_runs()
    print("✓ Passed")
    
    print("Test 2: Figure creation...")
    test_visualizar_parametros_ventilatorios_creates_figure()
    print("✓ Passed")
    
    print("Test 3: Edge cases...")
    test_visualizar_parametros_ventilatorios_with_edge_cases()
    print("✓ Passed")
    
    print("\nAll tests passed!")
