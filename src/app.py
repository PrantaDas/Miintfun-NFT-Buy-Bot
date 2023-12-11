import os
import asyncio
from dotenv import load_dotenv
from repository import Repository
from wallet import Wallet
from api import Api
from process_task import process_task


load_dotenv()

async def main():
    try:
        POLLING_INTERVAL = int(os.environ.get('INTERVAL','0'))

        repo = Repository(os.environ.get('MONGODB_URL'))

        await repo.start()

        wallet = Wallet(
        os.environ.get('PRIVATE_KEY'),
        os.environ.get('RPC_URL'),
        os.environ.get('GASS_LIMIT')
        )

        api = Api(
        os.environ.get('SDK_BASE_URL'),
        os.environ.get('MINT_FUN_BASE_URL'),
        os.environ.get('SDK_API_KEY'),
        os.environ.get('TRANSACTION_INFO_BASE_URL')
        )

        while True:
           await process_task(api,repo,wallet)
           await asyncio.sleep(POLLING_INTERVAL)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())