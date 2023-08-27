import pytest
from brownie import Token, accounts

@pytest.fixture(scope="function", autouse=True)
def shared_setup(module_isolation):
    pass

@pytest.fixture(scope="function")
def token(Token):
    return Token.deploy(100, {'from': accounts[0]})


