from brownie import Token, accounts

def deploy():
    deployer = accounts.load("1")
    token = Token.deploy(100, {'from': deployer})


def main():
    deploy()