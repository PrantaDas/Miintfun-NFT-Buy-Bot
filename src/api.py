from dotenv import load_dotenv
import requests as req

class Api:
    __api_Url:str
    __api_key:str
    __mintfun_base_url:str
    __transaction_info_baseurl:str

    def __init__(self, url, mintfun_url, key, trxn_url) -> None:
        self.__api_Url = url
        self.__api_key = key
        self.__mintfun_base_url = mintfun_url
        self.__transaction_info_baseurl = trxn_url
    

    async def mint(self, collection:str, taker:str, quantity:int, source:str):
        source
        if not source:
            source = "mint.fun"

        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'x-api-key': self.__api_key
        }

        payload = {
            'taker': taker,
            'source': source,
            'items':[
                {
                    'collection': collection.split(':')[1],
                    'quantity': quantity
                }
            ],
            'onlyPath': False,
            'partial': False,
            'skipBalanceCheck': True,
        }

        res = req.post(f"{self.__api_Url}/execute/mint/v1", headers = headers, json = payload)

        if res.status_code != 200: 
            print(f"=> {collection.split(':')[1]} Collection has no eligible mints.")
        
        return res.json()
    
    async def get_collection(self):
        res = req.get(self.__mintfun_base_url)
        if res.status_code != 200:
            res.raise_for_status()
        
        data = res.json()
        collections = data.get('collections',[])
        filtered_collections = filter(lambda item : 'userReported' not in item.get('flags',[]), collections)
        return list(filtered_collections)

    async def mint_qty(self,collection:str):
        response = req.get(f"{self.__transaction_info_baseurl}/{collection}/transactions")
        if response.status_code != 200:
            response.raise_for_status()
        
        data = response.json()
        transactions = data.get('transactions',[])
        return transactions

