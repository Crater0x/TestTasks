from brownie import Token, accounts
import brownie

TOKEN_BASE_URL = "https://black-legal-turkey-600.mypinata.cloud/ipfs/QmSnKuFFxDFiHuTMaoqBHCLPdnM6NFLy2PzgxqG5fN25Bj/"

def test_token_uri(token):
    token.mint(1, {'from': accounts[1], 'value': 1e15})
    assert token.tokenURI(0, {'from': accounts[1]}) == TOKEN_BASE_URL + "0.json"

def test_token_uri_invalid_id(token):
    with brownie.reverts("Token: invalid token ID"):
        token.tokenURI(0, {'from': accounts[1]})
