from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["PaoloTest"]

nbaroster = [
    {
        "id":1,
        "abbreviation":"ATL",
        "city":"Atlanta",
        "conference":"East",
        "division":"Southeast",
        "full_name":"Atlanta Hawks",
        "name":"Hawks",
        "titles": 1
    },
    {
        "id":2,
        "abbreviation":"BOS",
        "city":"Boston",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Boston Celtics",
        "name":"Celtics",
        "titles": 17
    },
    {
        "id":3,
        "abbreviation":"BKN",
        "city":"Brooklyn",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Brooklyn Nets",
        "name":"Nets",
        "titles": 0
    },
    {
        "id":4,
        "abbreviation":"CHA",
        "city":"Charlotte",
        "conference":"East",
        "division":"Southeast",
        "full_name":"Charlotte Hornets",
        "name":"Hornets",
        "titles": 0
    },
    {
        "id":5,
        "abbreviation":"CHI",
        "city":"Chicago",
        "conference":"East",
        "division":"Central",
        "full_name":"Chicago Bulls",
        "name":"Bulls",
        "titles": 6
    },
    {
        "id":6,
        "abbreviation":"CLE",
        "city":"Cleveland",
        "conference":"East",
        "division":"Central",
        "full_name":"Cleveland Cavaliers",
        "name":"Cavaliers",
        "titles": 1
    },
    {
        "id":7,
        "abbreviation":"DAL",
        "city":"Dallas",
        "conference":"West",
        "division":"Southwest",
        "full_name":"Dallas Mavericks",
        "name":"Mavericks",
        "titles": 1
    },
    {
        "id":8,
        "abbreviation":"DEN",
        "city":"Denver",
        "conference":"West",
        "division":"Northwest",
        "full_name":"Denver Nuggets",
        "name":"Nuggets",
        "titles": 0
    },
    {
        "id":9,
        "abbreviation":"DET",
        "city":"Detroit",
        "conference":"East",
        "division":"Central",
        "full_name":"Detroit Pistons",
        "name":"Pistons",
        "titles": 3
    },
    {
        "id":10,
        "abbreviation":"GSW",
        "city":"Golden State",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Golden State Warriors",
        "name":"Warriors",
        "titles": 7
    },
    {
        "id":11,
        "abbreviation":"HOU",
        "city":"Houston",
        "conference":"West",
        "division":"Southwest",
        "full_name":"Houston Rockets",
        "name":"Rockets",
        "titles": 2
    },
    {
        "id":12,
        "abbreviation":"IND",
        "city":"Indiana",
        "conference":"East",
        "division":"Central",
        "full_name":"Indiana Pacers",
        "name":"Pacers",
        "titles": 0
    },
    {
        "id":13,
        "abbreviation":"LAC",
        "city":"LA",
        "conference":"West",
        "division":"Pacific",
        "full_name":"LA Clippers",
        "name":"Clippers",
        "titles": 0
    },
    {
        "id":14,
        "abbreviation":"LAL",
        "city":"Los Angeles",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Los Angeles Lakers",
        "name":"Lakers",
        "titles": 17
    },
    {
        "id":15,
        "abbreviation":"MEM",
        "city":"Memphis",
        "conference":"West",
        "division":"Southwest",
        "full_name":"Memphis Grizzlies",
        "name":"Grizzlies",
        "titles": 0
    },
    {
        "id":16,
        "abbreviation":"MIA",
        "city":"Miami",
        "conference":"East",
        "division":"Southeast",
        "full_name":"Miami Heat",
        "name":"Heat",
        "titles": 3
    },
    {
        "id":17,
        "abbreviation":"MIL",
        "city":"Milwaukee",
        "conference":"East",
        "division":"Central",
        "full_name":"Milwaukee Bucks",
        "name":"Bucks",
        "titles": 2
    },
    {
        "id":18,
        "abbreviation":"MIN",
        "city":"Minnesota",
        "conference":"West",
        "division":"Northwest",
        "full_name":"Minnesota Timberwolves",
        "name":"Timberwolves",
        "titles": 0
    },
    {
        "id":19,
        "abbreviation":"NOP",
        "city":"New Orleans",
        "conference":"West",
        "division":"Southwest",
        "full_name":"New Orleans Pelicans",
        "name":"Pelicans",
        "titles": 0
    },
    {
        "id":20,
        "abbreviation":"NYK",
        "city":"New York",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"New York Knicks",
        "name":"Knicks",
        "titles": 2
    },
    {
        "id":21,
        "abbreviation":"OKC",
        "city":"Oklahoma City",
        "conference":"West",
        "division":"Northwest",
        "full_name":"Oklahoma City Thunder",
        "name":"Thunder",
        "titles": 1
    },
    {
        "id":22,
        "abbreviation":"ORL",
        "city":"Orlando",
        "conference":"East",
        "division":"Southeast",
        "full_name":"Orlando Magic",
        "name":"Magic",
        "titles": 0
    },
    {
        "id":23,
        "abbreviation":"PHI",
        "city":"Philadelphia",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Philadelphia 76ers",
        "name":"76ers",
        "titles": 3
    },
    {
        "id":24,
        "abbreviation":"PHX",
        "city":"Phoenix",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Phoenix Suns",
        "name":"Suns",
        "titles": 0
    },
    {
        "id":25,
        "abbreviation":"POR",
        "city":"Portland",
        "conference":"West",
        "division":"Northwest",
        "full_name":"Portland Trail Blazers",
        "name":"Trail Blazers",
        "titles": 1
    },
    {
        "id":26,
        "abbreviation":"SAC",
        "city":"Sacramento",
        "conference":"West",
        "division":"Pacific",
        "full_name":"Sacramento Kings",
        "name":"Kings",
        "titles": 1
    },
    {
        "id":27,
        "abbreviation":"SAS",
        "city":"San Antonio",
        "conference":"West",
        "division":"Southwest",
        "full_name":"San Antonio Spurs",
        "name":"Spurs",
        "titles": 5
    },
    {
        "id":28,
        "abbreviation":"TOR",
        "city":"Toronto",
        "conference":"East",
        "division":"Atlantic",
        "full_name":"Toronto Raptors",
        "name":"Raptors",
        "titles": 1
    },
    {
        "id":29,
        "abbreviation":"UTA",
        "city":"Utah",
        "conference":"West",
        "division":"Northwest",
        "full_name":"Utah Jazz",
        "name":"Jazz",
        "titles": 0
    },
    {
        "id":30,
        "abbreviation":"WAS",
        "city":"Washington",
        "conference":"East",
        "division":"Southeast",
        "full_name":"Washington Wizards",
        "name":"Wizards",
        "titles": 1
    }
]

#cancello tutto
db["Franchigie"].delete_many({})

#inserimento
db["Franchigie"].insert_many(nbaroster)

#or (item in db["Franchigie"])

#squadre per Conference
result = db.Franchigie.aggregate([
    {
        "$group": 
        { 
            "_id": "$conference",
            "teams": { "$sum": 1 }
        }
    }
])

print("")
print("Squadre per Conference:")
for r in result:
    print(r)

#titoli vinti per Division
result = db.Franchigie.aggregate([
    {
        "$group": 
        { 
            "_id": "$division",
            "titles": { "$sum": "$titles" }
        }
    }
])

print("")
print("Titoli vinti per Division:")
for r in result:
    print(r)

#titoli vinti per Division con condizione
result = db.Franchigie.aggregate([
    {
        "$group": 
        { 
            "_id": "$division",
            "titles": { "$sum": "$titles" }
        }
    },
    {
        "$match": { "titles": { "$gt": 10 } }    
    }
])

print("")
print("Titoli vinti per Division (> 10):")
for r in result:
    print(r)

#Prime 5 squadre per titoli vinti
result = db.Franchigie.aggregate([
    {
        "$sort": { "titles": -1 }
    },
    {
        "$project": { "_id": 0, "full_name": 1, "titles": 1}
    },
    {
        "$limit": 5
    }
])

print("")
print("Prime 5 squadre per titoli vinti:")
for r in result:
    print(r)

#titoli vinti e conteggio squadre per Division
result = db.Franchigie.aggregate([
    {
        "$group": 
        { 
            "_id": { "conference": "$conference", "division": "$division" },
            "count": { "$sum": 1 },
            "titles": { "$sum": "$titles" }
        }
    },
    {
        "$sort": { "_id": 1 }
    }    
])

print("")
print("Ttitoli vinti e conteggio squadre per Division:")
for r in result:
    print(r)

#media dei titoli vinti per Division:
result = db.Franchigie.aggregate([
    {
        "$group": 
        { 
            "_id": { "conference": "$conference", "division": "$division" },
            "count": { "$sum": 1 },
            "titles": { "$avg": "$titles" }
        }
    },
    {
        "$sort": { "titles": -1 }
    }    
])

print("")
print("Media dei titoli vinti per Division:")
for r in result:
    print(r)

#valore minimo e valore massimo di titoli vinti per Division:
result = db.Franchigie.aggregate([
    {
        "$group": 
        { 
            "_id": { "conference": "$conference", "division": "$division" },
            "min_titles": { "$min": "$titles" },
            "max_titles": { "$max": "$titles" }
        }
    },
    {
        "$sort": { "_id": 1 }
    }    
])

print("")
print("Valore minimo e valore massimo di titoli vinti per Division")
for r in result:
    print(r)