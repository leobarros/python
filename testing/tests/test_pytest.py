from codigo.jogo import brincadeira

"""
O teste é formado por 3 etapas (GWT)
- Given - Dado
- When  - Quando
- Then  - Então

Outra é chamada de (AAA)
- Arange
- Act
- Assert
"""

def test_quando_bricadeira_receber_1_entao_deve_retornar_1():
    assert brincadeira (1) == 1

def test_quando_bricadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira (2) == 2

def test_quando_bricadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira (3) == 'queijo'

def test_quando_bricadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira (5) == 'goiabada'