from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["PaoloTest"]
#db = client.PaoloTest

libri = [
    {
        "id": 1,
        "isbn": "0123ABC",
        "titolo": "La Divina Commedia - Inferno",
        "id_autore": 1,
        "prezzo": 28.5,
        "editore": "Zanichelli"
    },
    {
        "id": 2,
        "isbn": "0456ABC",
        "titolo": "La Divina Commedia - Purgatorio",
        "id_autore": 1,
        "prezzo": 28.5,
        "editore": "Zanichelli"
    },
    {
        "id": 3,
        "isbn": "0789ABC",
        "titolo": "La Divina Commedia - Paradiso",
        "id_autore": 1,
        "prezzo": 28.5,
        "editore": "Zanichelli"
    },
    {
        "id": 4,
        "isbn": "0123XYZ",
        "titolo": "I Promessi Sposi",
        "id_autore": 2,
        "prezzo": 25,
        "editore": "Zanichelli"
    },
    {
        "id": 5,
        "isbn": "9999ABC",
        "titolo": "Guida galattica per autostoppisti",
        "id_autore": 3,
        "prezzo": 28.5,
        "editore": "Mondadori"
    }
]

autori = [
    {
        "id": 1,
        "nome": "Dante Alighieri"
    },
    {
        "id": 2,
        "nome": "Alessandro Manzoni"
    },
    {
        "id": 3,
        "nome": "Douglas Adams"
    }
]

#svuoto tutto
res = db.Libri.delete_many({}) 
res = db.Autori.delete_many({}) 

#inserimento
res = db.Libri.insert_many(libri)
res = db.Autori.insert_many(autori)


docs = db.Libri.aggregate([{"$lookup":{
            "from": "Autori",           # altra collection
            "localField": "id_autore",  # campo chiave della collection su cui invoco il metodo aggregate
            "foreignField": "id",       # campo chiave dell'altra collection 
            "as": "dati_autore"         # alias per il set di dati risultante
        }},
        #tramite questo parametro stabilisco quali campi visualizzare
        {"$project": {"_id": 0, "titolo": 1, "editore": 1, "prezzo": 1, "dati_autore": { "nome": 1}}}
])

print("Join Libri -> Autori")
for doc in docs:        
    print(doc)

print("")
print("")

docs = db["Autori"].aggregate([{"$lookup":{
            "from": "Libri",                # altra collection
            "localField": "id",             # campo chiave della collection su cui invoco il metodo aggregate
            "foreignField": "id_autore",    # campo chiave dell'altra collection 
            "as": "dati_libri"              # alias per il set di dati risultante
#        }}
#])        
        }},
        #tramite questo parametro stabilisco quali campi visualizzare
        {"$project": {"_id": 0, "nome": 1, "dati_libri": { "titolo": 1}}}
])

print("Join Autori -> Libri")
for doc in docs:        
    print(doc)
