# from web3 import Web3
# from eth_account import Account
# infura_url = 'https://mainnet.infura.io/v3/74c8cc91eb3c438b808f2b154fc49736'
#
# web3 = Web3(Web3.HTTPProvider(infura_url))
# # print(web3.is_connected())
# # print(web3.eth.block_number)
# # balance = web3.eth.get_balance("0x53667336d94F053D24283a470B82D1EaB464678D")
# # print(balance)
# # print(web3.from_wei(balance, 'ether'))
#
# network_id = web3.net.version
# print(f"Connected to network with ID: {network_id}")
# # account = Account.create()
# # print(f"New account created: {account.address}")
# # print(f"Private key: {account._private_key.hex()}")
#
# private_key = '0x3e32d372f7c3245cc16441877cc9d56c66d50db669cba1ff630e7ec65861862c'
# account=Account.from_key(private_key)
# print(f"Loaded account: {account.address}")
#
# balance = web3.eth.get_balance(account.address)
# print(f"Account balance: {web3.from_wei(balance, 'ether')} ETH")
#
# contract_address = 'CONTRACT_ADDRESS'
# contract_abi=[...]
# # Your contract ABI contract=w3.eth.contract(address=contract_address, abi=contract_abi)
#
# balance=contract_address.functions.getBalance(account.address).call()
# print(f"Contract balance: {balance}")

from web3 import Web3
from eth_account import Account

infura_url = 'https://mainnet.infura.io/v3/74c8cc91eb3c438b808f2b154fc49736'
web3 = Web3(Web3.HTTPProvider(infura_url))

# DAI contract address and ABI
contract_address = '0x8d35026d681972f0ac7d6ffb5f9906b59acbc8ebf9d9abc1824dae7953e4f598'
contract_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]

# Creating a contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with the account address you want to check
account_address = '0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe'

# Fetching the balance
balance = contract.functions.balanceOf(account_address).call()
print(f"DAI Balance of account {account_address}: {balance}")

to_address = 'RECIPIENT_ADDRESS' amount=100 # Number of tokens to transfer transaction=contract.functions.transfer(to_address, amount).buildTransaction({ 'from': account.address, 'nonce': w3.eth.getTransactionCount(account.address), 'gas': 200000, 'gasPrice': w3.toWei('40', 'gwei') }) signed_txn=w3.eth.account.signTransaction(transaction, account.privateKey) transaction_hash=w3.eth.sendRawTransaction(signed_txn.rawTransaction) print(f"Transaction sent: {transaction_hash.hex()}")