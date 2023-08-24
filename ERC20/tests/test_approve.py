from brownie import accounts, Token

def test_approve_function():
    deployer=accounts[0]
    initial_supply=1000000
    amount = 100000
    accounts_to = [i.address for i in accounts]
    token=Token.deploy(initial_supply, amount, accounts_to[0:1], {'from': deployer})

    spender = accounts[1]
    to = accounts[2]
    amount_spend = 100
    amount_transfer = 50

    token.approve(spender, amount_spend, {'from': deployer})

    token.transferFrom(deployer, to, amount_transfer, {'from': spender})

    assert token.balanceOf(deployer) == amount - amount_transfer
    assert token.balanceOf(to) == amount_transfer

    assert token.allowance(deployer, spender) == amount_spend - amount_transfer



