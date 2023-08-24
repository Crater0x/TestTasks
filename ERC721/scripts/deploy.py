from brownie import Token, accounts

def deploy():
    deployer = accounts[0]
    token = Token.deploy(100, {'from': deployer})

    print("Token deployed to:", token.address, token.balanceOf(token.address))

    for i  in range(len(accounts)):
        print(i, accounts[i].address, token.balanceOf(accounts[i]), token.getBalance(accounts[i]), accounts[i].balance())


    # token.mint(1, {'from': accounts[1], 'value': 10**15})
    token.mint(3, {'from': accounts[1], 'amount': 3 * 10**18})

    for i  in range(len(accounts)):
        print(i, accounts[i].address, token.balanceOf(accounts[i]), token.getBalance(accounts[i]), accounts[i].balance())




def main():
    deploy()