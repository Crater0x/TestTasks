from brownie import accounts, Token

def test_token_balancet():
    balance = accounts[0].balance()
    accounts[0].transfer(accounts[1], "10 ether", gas_price=0)

    assert balance - "10 ether" == accounts[0].balance()
    

def test_token_deployment():
    deployer = accounts[0]
    initial_supply = 1000000

    # Deploy the token contract
    token = Token.deploy(initial_supply, {'from': deployer})

    # Verify the deployment
    # assert token.owner() == deployer
    assert token.totalSupply() == initial_supply