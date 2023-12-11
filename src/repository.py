from pymongo.mongo_client import MongoClient

class Repository:

    def __init__(self,mongo_uri:str) -> None:
        self.client = MongoClient(mongo_uri)
        match = mongo_uri.split('/')[3].split('?')[0] if len(mongo_uri.split('/')) > 3 else 'test'
        self.db = self.client.get_database(match)
        self.collection = self.db.get_collection('mint')


    async def start(self):
        try:
            print("=> Connecting to MONGODB")
            
            self.client.server_info()
            print("=> Connected to MONGODB")

        except Exception as e:
            print(e)

    async def find(self,args):
        try:
            collections = []
            docs = self.collection.find(args)

            if  docs.count() == 0:
                print('No such Document found...')
            
            for doc in docs:
                collections.append(doc)
            
            return collections

        except Exception as e:
            print(e)
    
    def insertOne(self,args):
        try:
            new_mint = self.collection.insert_one(args)
            inserted_id = new_mint.inserted_id
            return self.collection.find_one({"_id":inserted_id})

        except Exception as e:
            print(e)
    
    def findOne(self,args):
        try:
            doc = self.collection.find_one(args)
            return doc
        except Exception as e:
            print(e)