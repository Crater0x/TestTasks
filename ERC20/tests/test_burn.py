from brownie import accounts, Token

def test_burn_function():
    deployer=accounts[0]
    initial_supply=1000000
    amount_in = 100000

    accounts_to = [i.address for i in accounts]

    token=Token.deploy(initial_supply, amount_in, accounts_to, {'from': deployer})

    to = accounts[1]


    assert token.balanceOf(to) == amount_in

    token.burn(to, amount_in, {'from': deployer})


    assert token.balanceOf(to) == 0

