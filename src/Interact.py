from web3 import Web3
from Deploy import deploy_contract
import os

# Load environment variables
contract_file = "src/newContract.sol"
contract_name = "newContract"
account = os.getenv("ANVIL_ACCOUNT")
private_key = os.getenv("ANVIL_PRIVATE_KEY")
provider = os.getenv("LOCAL_PROVIDER")
chain_id = int(os.getenv("CHAIN_ID", 31337))  

print(provider)


connection = Web3(Web3.HTTPProvider(provider))

contract_address, abi = deploy_contract(contract_file, contract_name, account, private_key, provider, chain_id)
print(f"Contract deployed at {contract_address}")

contract = connection.eth.contract(address=contract_address, abi=abi)

initial_value = contract.functions.viewMyId().call()
print(f"Initial value is {initial_value}")

nonce = connection.eth.get_transaction_count(account)

print("Creating Transactions")

transaction = contract.functions.updateID(5341).build_transaction({
    "chainId": chain_id,
    "gasPrice": connection.eth.gas_price,
    "from": account,
    "nonce": nonce
})


signed_txn = connection.eth.account.sign_transaction(transaction, private_key=private_key)
print("Updated stored Value")
tx_hash = connection.eth.send_raw_transaction(signed_txn.raw_transaction)

tx_receipt = connection.eth.wait_for_transaction_receipt(tx_hash)
print("updated")

updated_value = contract.functions.viewMyId().call()
print(f"Updated value is {updated_value}")
