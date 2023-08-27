from brownie import accounts, Token, network, config, interface

def deploy_test():
    deployer=accounts[0]
    initial_supply=1000000
    amount_in = 100000
    accounts_to = [i.address for i in accounts]
    token=Token.deploy(initial_supply, amount_in, accounts_to[0:1], {'from': deployer})

    print(f'Token deployed at address: {token.address}\n')
    for i  in range(len(accounts)):
        print(i, accounts[i].address, token.balanceOf(accounts[i]))

    print(token.totalSupply())

def deploy_sepolia():
    network_name = network.show_active()

    print(network_name)

    if network_name not in config["networks"]:
        print(f"{network_name} network not found in the configuration file!")
        return


    deployer = accounts.load("1")

    initial_supply=1000000
    amount_in = 100000
    accounts_to = [i.address for i in accounts]
    token=Token.deploy(initial_supply, amount_in, accounts_to[0:1], {'from': deployer})

def main():
    deploy_sepolia()