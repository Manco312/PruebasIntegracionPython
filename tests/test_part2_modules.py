
from modules.discount import DiscountEngine
from modules.order import OrderCalculator

def test_order_calculator_uses_discount_engine():
    de = DiscountEngine()
    calc = OrderCalculator(de)

    assert calc.final_total(250.0, 0.19) == 252.88
    assert calc.final_total(120.0, 0.19) == 128.52
    assert calc.final_total(60.0, 0.19) == 67.83
    assert calc.final_total(40.0, 0.19) == 47.6


"""
Explica por qué esta es una prueba de integración (y no solo unitaria).

Esta es una prueba de integración porque verifica la colaboración entre dos módulos diferentes: 
el módulo de descuento y el módulo de cálculo de pedidos.
La prueba no solo verifica la lógica interna de cada módulo por separado, sino que también asegura
que el OrderCalculator utilice correctamente el DiscountEngine para calcular el total final.
"""
