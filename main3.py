from MongoWrapper import MongoWrapper

wrp = MongoWrapper("PaoloTest")

macchine = [
     {
        "id": 1,
        "modello": "127",
        "marca": "Fiat",
        "prezzo": 1300,
        "velocitamax": 110,
        "dimensioni": [380, 140, 160]
    },
    {
        "id": 2,
        "modello": "Giulietta",
        "marca": "Alfa Romeo",
        "prezzo": 4000,
        "velocitamax": 180,
        "dimensioni": [425, 148, 165]
    },
    {
        "id": 3,
        "modello": "Fiesta",
        "marca": "Ford",
        "prezzo": 1600,
        "velocitamax": 130,
        "dimensioni": [385, 145, 160]
    },
    {
        "id": 4,
        "modello": "Baracca",
        "marca": "Subaru",
        "prezzo": 5500,
        "velocitamax": 170,
        "dimensioni": [430, 148, 166]
    },
    { 
        "id": 5, 
        "modello": "Polo", 
        "marca": "Volkswagen", 
        "prezzo": 1400, 
        "velocitamax": 120,
        "dimensioni": [385, 140, 160] 
    }
]


#svuoto tutto
res = wrp.delete("Macchine", {})

#inserimento
res = wrp.insert("Macchine", macchine)
#print("Inserimento multiplo: " + str(res))
#print("")

menu = "\nSeleziona un'operazione:"
menu += "\n0: Esci"
menu += "\n1: Lettura di tutti i document"
menu += "\n2: Ricerca con valore esatto"
menu += "\n3: Ricerca con criterio"
menu += "\n4: Ricerca con condizioni in AND"
menu += "\n5: Ricerca con condizioni in OR"
menu += "\n6: Ricerca con RegEx"
menu += "\n7: Ricerca all'interno di un array (1 valore)"
menu += "\n8: Ricerca all'interno di un array (più valori)"
menu += "\n9: Ricerca con specifica dei campi"
menu += "\n"

scelta = -1
while (scelta != 0):
    scelta = int(input(menu))
    #print("Hai scelto -> " + str(scelta))

    if scelta == 1: 
        #lettura
        print("Lettura:")
        res = wrp.find("Macchine")
        for document in res:
            print(document)

    elif scelta == 2:
        #ricerca con valore esatto
        print("Macchina modello Giulietta:")
        criteria = { "modello": "Giulietta" }
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 3:
        #ricerca con criterio
        print("Macchine con velocità superiore a 150")
        criteria = { "velocitamax": { "$gt": 150 } }
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 4:
        #condizioni in AND
        print("Macchine con prezzo inferiore a 1500 € e marca Volkswagen:")
        criteria = { "prezzo": { "$lt": 1500 }, "marca": "Volkswagen" }
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 5:
        #condizioni in OR (+ clausola IN)
        print("Macchine con prezzo inferiore a 1500 € oppure marca Subaru o Ford")
        criteria = { "$or": [{"prezzo": { "$lt": 1500 }}, {"marca": { "$in": ["Subaru", "Ford"]}}]}
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 6:
        #utilizzo di regular expressions
        print("Macchine con marca che inizia per 'F':")
        criteria = { "marca": { "$regex": "^F" } }
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 7:
        #ricerca all'interno di array (presenza di un valore)
        print("Macchine con una dimensione pari a 160:")
        criteria = { "dimensioni": 160 }
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 8:
        #ricerca all'interno di array (presenza di più valori)
        print("Macchine con una dimensione pari a 160 ed un'altra pari a 140:")
        criteria = { "dimensioni": { "$all": [160, 140]} }
        res = wrp.find("Macchine", criteria)
        for document in res:
            print(document)

    elif scelta == 9:
        #specifica dei campi
        print("Macchine con prezzo maggiore di 3000 €, selezionando solo marca e modello:")
        criteria = { "prezzo": { "$gt": 3000} }
        projection = { "_id": 0, "marca": 1, "modello": 1}
        res = wrp.find("Macchine", criteria, "", projection)
        for document in res:
            print(document)

    else:
        if scelta != 0:
            print("non fare lo spiritoso...")
