from brownie import Token, accounts

def deploy():
    # Get the deployer's account
    deployer = accounts[0]

    # Deploy the token contract
    token = Token.deploy({'from': deployer})

    print("Token deployed to:", token.address)

def main():
    deploy()