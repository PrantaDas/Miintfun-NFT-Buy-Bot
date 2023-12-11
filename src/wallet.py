from web3 import Web3

class Wallet:

    def __init__(self, private_key:str, rpc_url:str, gass_limit:int):
       self.__rpc = rpc_url
       self.__key = private_key
       self.__nonce_offset = 0
       self.__gas_limit = int(gass_limit,10)
       self.wallet = self.create_wallet()

    
    @property
    def provider(self):
        return Web3(Web3.HTTPProvider(self.__rpc))
    
    def create_wallet(self):
        return  self.provider.eth.account.from_key(self.__key)
    
    def get_nonce(self):
        res = self.provider.eth.get_transaction_count(self.wallet.address)
        nonce = res + self.__nonce_offset
        self.__nonce_offset += 1
        return  nonce

    async def estimate_gas_prise(self):
        gas_price = self.provider.eth.gas_price
        return gas_price
    
    async def estimate_gas_limit(self):
        block_info = self.provider.eth.get_block('latest')
        return block_info['gasLimit']
    
    async def get_feed_data(self):
        feed_data = self.provider.eth.get_block('latest')
        return feed_data
    
    def send_transaction (self,data):
    
        transaction_data = {
            'to': Web3.to_checksum_address(data.get('to')),
            'value': int(data['value'],16),
            'gas': self.__gas_limit,
            'nonce':  self.get_nonce(),
            'data': data['data'],
            'from' : Web3.to_checksum_address(data['from'])
        }

        raw_transactions = self.provider.eth.send_transaction(transaction_data)
        return raw_transactions.hex()