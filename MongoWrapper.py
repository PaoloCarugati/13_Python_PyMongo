import pymongo

class MongoWrapper:
    def __init__(self, db, connectionstring = "mongodb://localhost:27017/"):
        self._client = pymongo.MongoClient(connectionstring)
        self._database = self._client[db]


    #inserisce documents (che può essere un documento singolo o un array)
    #all'interno della collection collectionname
    def insert(self, collectionname, documents):
        res = False
        try:
            collection = self._database[collectionname]
            if type(documents) == list:
                res = collection.insert_many(documents)
            else:
                res = collection.insert_one(documents)
            res = True
        except Exception as e:
            print(e)
        return res


    #restituisce i documenti presenti all'interno della collection collectionname
    def find(self, collectionname, filter = None, sortby = "", projection = {}):
        res = None
        try:
            collection = self._database[collectionname]
            if filter == None:
                res = collection.find(projection = projection)
            else:
                res = collection.find(filter=filter, projection = projection)
            if sortby != "":
                res = res.sort(sortby)
        except Exception as e:
            print(e)
        return res


    #aggiorna i documenti della collection collectionname che
    #corrispondono ai criteri criteria assegnando loro i nuovi valori values
    def update(self, collectionname, criteria, values):
        res = False
        try:
            collection = self._database[collectionname]
            collection.update_many(criteria, values)
            res = True
        except Exception as e:
            print(e)
        return res
    

    #elimina dalla collection collectionname i documenti che hanno
    #una corrispondenza con criteria
    def delete(self, collectionname, criteria):
        res = False
        try:
            collection = self._database[collectionname]
            collection.delete_many(criteria)
            res = True
        except Exception as e:
            print(e)
        return res

