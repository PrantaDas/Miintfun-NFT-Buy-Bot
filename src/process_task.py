from api import Api
from repository import Repository
from wallet import Wallet


async def process_task(api: Api, repo: Repository, wallet: Wallet):
    try:
        # Get the collection
        collections = await api.get_collection()
        
        # Iterate over the collections
        for collection in collections:
            is_exist = repo.findOne({'collAddress':collection['contract'].split(':')[1],'name':collection['name']})

            if is_exist:
                print(f"=> {collection['contract']} is already minted.Skipping...")
                continue

            transaction_info = await api.mint_qty(collection['contract'])
            # min_transaction = min(transaction_info, key = lambda trxn: int(trxn['nftCount'])) if transaction_info else None
            # quantity = int(min_transaction['nftCount']) if min_transaction and int(min_transaction['nftCount']) > 0 else 1
            # # print(wallet.wallet.address)
            # quantity = int(quantity)

            nft_counts = [int(trxn['nftCount']) for trxn in transaction_info]
            min_transaction = min(transaction_info, key=lambda trxn: nft_counts) if transaction_info else None
            quantity = min_transaction['nftCount'] if min_transaction and int(min_transaction['nftCount']) > 0 else 1

            # Perform the synchronous int conversion outside the await block
            quantity = int(quantity)

            mint_response = await api.mint(collection['contract'], wallet.wallet.address, quantity, "mint.fun")
            if (
                mint_response is not None
                and 'steps' in mint_response
                and mint_response['steps']
                and 'items' in mint_response['steps'][0]
                and mint_response['steps'][0]['items']
                and mint_response['steps'][0]['items'][0]
              ):
                data = mint_response['steps'][0]['items'][0]['data']
                trxn_info = wallet.send_transaction(data)
                
                if trxn_info and trxn_info is not None:
                    minted = repo.insertOne({'name':collection['name'],'collAddress':collection['contract'].split(':')[1],'trxId':trxn_info})
                    if minted and minted is not None:
                        print(f"=> New Collection minted Transaction Hash: {trxn_info}")
    except Exception as e:
        print(e)