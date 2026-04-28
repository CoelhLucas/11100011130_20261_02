from unittest.mock import patch

import pytest

from src.main import *


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def  test_lucas():
    with patch('random.randint', return_value=12345):
        result = await lucas()
    assert result == {"Test": True, "Num aleatorio": 12345}

@pytest.mark.asyncio
async def  test_estudante_cadastro():
    estudante_teste = Estudante(nome="Nome", curso="curso", ativo=False)
    result = await estudante_cadastro(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def  test_estudante_update_negativo():
    result = await estudante_update(-5)
    assert not result

@pytest.mark.asyncio
async def  test_estudante_update_positivo():
    result = await estudante_update(10)
    assert result

@pytest.mark.asyncio
async def  test_estudante_delete_negativo():
    result = await estudante_delete(-5)
    assert not result

@pytest.mark.asyncio
async def  test_estudante_delete_positivo():
    result = await estudante_delete(10)
    assert result
