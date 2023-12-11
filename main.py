#check EVM balance from all available chains
from web3 import Web3

#RPC
polygon_url = 'https://polygon-rpc.com'

#Smart contract
token_address = '0x60e6895184448f3e8ef509d083e3cc3ac31f82fd'
address = '0xC62DC5C6f306E67BF1e9D0346b579000Bc88b6c4'

#Connection
web3 = Web3(Web3.HTTPProvider(polygon_url))
print('connection', web3.is_connected())

#check balance
file = open('wallet.txt')
total = 0
stt = 0
for line in file:
    balance = web3.eth.get_balance(line.strip())
    eth = web3.from_wei(balance,'ether')
    tx_count = web3.eth.get_transaction_count(line.strip())

    print(f'Wallet {stt}:', round(eth, 4),'ETH ----', tx_count, "transactions")
    total += eth
    stt += 1

#print total balance
print('total =', round(total, 4), "ETH")
