from brownie import Token, accounts
import brownie

def test_mint_tokens(token):
    token.mint(3, {'from': accounts[1], 'value': 3e15})

    assert token.balanceOf(accounts[1]) == 3
    assert accounts[1].balance() == int(1e20 - 3e15)
    assert accounts[0].balance() == 1e20 + 3e15
    

def test_mint_limit(token):
    with brownie.reverts("Token: NFT mint limit reached!"):
        token.mint(4, {'from': accounts[1], 'value': 3e15})

def test_mint_token_balance(token):
    token.mint(3, {'from': accounts[1], 'value': 3e15})
    token.mint(3, {'from': accounts[1], 'value': '0.003 ether'})

    assert token.balanceOf(accounts[1]) == 6
    with brownie.reverts("Token: address could own less then 6 tokens!"):
        token.mint(1, {'from': accounts[1], 'value': 1e15})


def test_mint_max_total_supply(token):
    for account in accounts:
        token.mint(3, {'from': account, 'value': '0.003 ether'})

    token.mint(1, {'from': accounts[1], 'value': 1e15})
    assert token.currentId() == 100

    with brownie.reverts("Token: max token amount reached!"):
        token.mint(1, {'from': accounts[1], 'value': 1e15})


def test_mint_fee_amount(token):
    with brownie.reverts("Token: Insufficient fee amount"):
        token.mint(1, {'from': accounts[1], 'value': 1e15 - 1})
