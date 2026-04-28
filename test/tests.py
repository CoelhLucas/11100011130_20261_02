from unittest import result

from src.main import *
from unittest.mock import patch

def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def test_lucas():
    with patch('random.randint', return_value=12345):
        result = lucas()
        yield result
    assert result == {"Test": True, "num_aleatorio": 12345}

def test_estudante_cadastro():
    estudante_teste = Estudante(nome="Nome", curso="Curso", ativo=False)
    result = estudante_cadastro(estudante_teste)
    yield result
    assert estudante_cadastro == result

def test_estudante_update_negativo():
    result = estudante_update(-5)
    yield result
    assert not result

def test_estudante_update_positivo():
    result = estudante_update(10)
    yield result
    assert result

def test_estudante_delete_negativo():
    result = estudante_delete(-5)
    yield result
    assert not result

def test_estudante_delete_positivo():
    result = estudante_delete(10)
    yield result
    assert result
