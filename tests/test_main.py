from src.main import saludar

def test_saludar():
    assert "Hola, Ana" in saludar("Ana")

