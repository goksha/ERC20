from web3 import Web3
from decouple import config

infura_url = config('INFURA_URL')

contractAddress = Web3.toChecksumAddress(config('CONTRACT_ADDRESS'))

ownerAddress = Web3.toChecksumAddress(config('OWNER_ADDRESS'))
Private_Key = config('SUPER_SECRET_PRIVATE_KEY')

abi='[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

web3 = Web3(Web3.HTTPProvider(infura_url))

#Functions

def getSymbol():
    web3 = Web3(Web3.HTTPProvider(infura_url))
    res = web3.isConnected()
    if res:
        contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
        symbol = contract_instance.functions.symbol().call()
        return symbol
# gets the balance of the provided account
def balanceOf(account):
    web3 = Web3(Web3.HTTPProvider(infura_url))
    res = web3.isConnected()
    if res:
        contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
        bal = contract_instance.functions.balanceOf(account).call()
        return bal
# gets the token decimals
def getDecimals():
    web3 = Web3(Web3.HTTPProvider(infura_url))
    res = web3.isConnected()
    if res:
        contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
        decimals = contract_instance.functions.decimals().call()
        return str(decimals)
# gets the total supply of the token
def totalSupply():
    web3 = Web3(Web3.HTTPProvider(infura_url))
    res = web3.isConnected()
    if res:
        contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
        symbol = contract_instance.functions.balanceOf(ownerAddress).call()
        return symbol

res = web3.isConnected()
print(res)

if res:
    print("Name is: " + getSymbol())
    print("symbol is: " + getSymbol())
    print("decimal is: " + getDecimals())
    print("balance is : " + str(balanceOf(ownerAddress)))

decimals = 10 ** 18
bal = balanceOf(ownerAddress) / decimals
targetBalance = bal / decimals


