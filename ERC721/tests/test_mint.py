from brownie import Token, accounts

def test_mint_function():
    # Get the deployer's account
    deployer = accounts[0]

    # Deploy the token contract
    token = Token.deploy(100, {'from': deployer})

    print("Token deployed to:", token.address)

    token.mint(3, {'from': accounts[1], 'value': 10**15})

    print(accounts[1].balacne())
    print(accounts[0].balacne())
