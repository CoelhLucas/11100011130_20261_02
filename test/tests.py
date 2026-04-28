from src.main import *
from unittest.mock import patch


def test_root():
    assert root() == {"message": "Hello World"}

def test_lucas():
    with patch('random.randint', return_value=12345):
        result = lucas();
    assert result == {"Test": True, "num_aleatorio": 12345}

def test_estudante_cadastro():
    estudante_teste = Estudante(nome="Nome", curso="Curso", ativo=False)
    assert estudante_teste == estudante_cadastro(estudante_teste)

def test_estudante_update_negativo():
    assert not estudante_update(-5)

def test_estudante_update_positivo():
    assert estudante_update(10)

def test_estudante_delete_negativo():
    assert not estudante_delete(-5)

def test_estudante_delete_positivo():
    assert estudante_delete(10)

