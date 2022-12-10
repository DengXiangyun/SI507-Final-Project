import json
import csv
import pandas as pd

SRC_JSON = 'SoFIFAdata.json'
SRC = open(SRC_JSON, 'r', encoding='utf-8-sig')
SoFIFAdata = json.loads(SRC.read())
SRC.close()

Leagues = ["Premier League", "Bundesliga", "La Liga", "Serie A", "Ligue 1", "Others"]
column = ['Team', 'Team_Image', 'League Id']
Teamdata = pd.DataFrame(columns = column)
Team = []
for i in SoFIFAdata:
    if i['Team'] not in Team:
        Team.append(i['Team'])
        team = i["Team"]
        team_image = i["Team Image"]
        league = i["League"]
        for j in range(len(Leagues)):
            if league == Leagues[j]:
                league_id = j+1
        team_data = pd.DataFrame([[team, team_image, league_id]])
        team_data.columns = column
        Teamdata = Teamdata.append(team_data, ignore_index = True)

print(Teamdata.head()) 

Teamdata.to_csv('Teamdata.csv', index = None, encoding='utf-8-sig')


# column = ['Nation', 'Nation Image']
# Nationdata = pd.DataFrame(columns = column)
# Nation = []
# for i in SoFIFAdata:
#     if i["Nationality"] not in Nation:
#         Nation.append(i["Nationality"])
#         nation = i["Nationality"]
#         nation_image = i["Flag"]
#         nation_data = pd.DataFrame([[nation, nation_image]])
#         nation_data.columns = column
#         Nationdata = Nationdata.append(nation_data, ignore_index = True)

# print(Nationdata.head()) 

# Nationdata.to_csv('Nationdata.csv', index = None, encoding='utf-8-sig')


# def csv_to_json(csvFilePath, jsonFilePath):
#     jsonArray = []
      
#     #read csv file
#     with open(csvFilePath, encoding='utf-8-sig') as csvf: 
#         #load csv file data using csv library's dictionary reader
#         csvReader = csv.DictReader(csvf) 

#         #convert each csv row into python dict
#         for row in csvReader: 
#             #add this python dict to json array
#             jsonArray.append(row)
  
#     #convert python jsonArray to JSON String and write to file
#     with open(jsonFilePath, 'w', encoding='utf-8-sig') as jsonf: 
#         jsonString = json.dumps(jsonArray, indent=4)
#         jsonf.write(jsonString)


# csvFilePath = r'Teamdata.csv'
# jsonFilePath = r'Teams.json'
# csv_to_json(csvFilePath, jsonFilePath)

# SRC_JSON = 'Teams.json'
# SRC = open(SRC_JSON, 'r', encoding='utf-8-sig')
# Teamdata = json.loads(SRC.read())
# SRC.close()


# for team in Teamdata:
#     team["League Id"] = int(team["League Id"])
#     team["Overall"] = int(team["Overall"])

# with open("Teams.json", "w") as fp:
#     json.dump(Teamdata, fp, indent=4)
 
# fp.close()


# csvFilePath = r'Nationdata.csv'
# jsonFilePath = r'Nations.json'
# csv_to_json(csvFilePath, jsonFilePath)

# SRC_JSON = 'Nations.json'
# SRC = open(SRC_JSON, 'r', encoding='utf-8-sig')
# Nationdata = json.loads(SRC.read())
# SRC.close()

# for nation in Nationdata:
#     nation["Ranking"] = int(nation["Ranking"])

# with open("Nations.json", "w") as fp:
#     json.dump(Nationdata, fp, indent=4)
 
# fp.close()

# csvFilePath = r'Leagues.csv'
# jsonFilePath = r'Leagues.json'
# csv_to_json(csvFilePath, jsonFilePath)

# SRC_JSON = 'Leagues.json'
# SRC = open(SRC_JSON, 'r', encoding='utf-8-sig')
# Leaguedata = json.loads(SRC.read())
# SRC.close()

# for league in Leaguedata:
#     league["ID"] = int(league["ID"])

# with open("Leagues.json", "w") as fp:
#     json.dump(Leaguedata, fp, indent=4)
 
# fp.close()


