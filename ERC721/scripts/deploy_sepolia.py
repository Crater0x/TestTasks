from brownie import Token, accounts

TOKEN_BASE_URL = "https://black-legal-turkey-600.mypinata.cloud/ipfs/QmSnKuFFxDFiHuTMaoqBHCLPdnM6NFLy2PzgxqG5fN25Bj/"

def deploy():
    deployer = accounts.load("1")
    token = Token.deploy(100, TOKEN_BASE_URL, {'from': deployer})


def main():
    deploy()