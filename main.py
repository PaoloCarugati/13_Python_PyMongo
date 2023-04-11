from MongoWrapper import MongoWrapper

wrp = MongoWrapper("PaoloTest")

macchine = [
     {
        "id": 1,
        "modello": "127",
        "marca": "Fiat",
        "prezzo": 1300,
        "velocitamax": 110
    },
    {
        "id": 2,
        "modello": "Giulietta",
        "marca": "Alfa Romeo",
        "prezzo": 4000,
        "velocitamax": 180
    },
    {
        "id": 3,
        "modello": "Fiesta",
        "marca": "Ford",
        "prezzo": 1600,
        "velocitamax": 130
    },
    {
        "id": 4,
        "modello": "Baracca",
        "marca": "Subaru",
        "prezzo": 5500,
        "velocitamax": 170
    }
]

macchina = { 
    "id": 5, 
    "modello": "Polo", 
    "marca": "VW", 
    "prezzo": 1400, 
    "velocitamax": 120 
}


#inserimento
res = wrp.insert("Macchine", macchine)
print("Inserimento multiplo: " + str(res))
res = wrp.insert("Macchine", macchina)
print("Inserimento singolo: " + str(res))

print("")

#lettura
print("Lettura:")
res = wrp.find("Macchine")
for document in res:
    print(document)

print("")

#modifica
criteria = { "marca": "VW" }
values = { "$set": { "marca": "Volkswagen" }}
res = wrp.update("Macchine", criteria, values)
print("Modifica: " + str(res))

print("")

#lettura dei soli record modificati
print("Lettura con filtro:")
res = wrp.find("Macchine", { "marca": "Volkswagen" })
for document in res:
    print(document)

print("")

#cancellazione
res = wrp.delete("Macchine", { "prezzo": 5500 })
print("Cancellazione: " + str(res))

print("")

#rifaccio la lettura in ordine di velocità 
print("Lettura con ordinamento:")
res = wrp.find("Macchine", None, "velocitamax")
for document in res:
    print(document)
