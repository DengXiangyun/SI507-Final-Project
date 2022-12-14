import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as Soup
import csv
import json
import sqlite3

SoFIFA_url = "https://sofifa.com/players?offset="
column = ['ID','picture','Flag','Name','Age','Position','Nationality','Overall','Potential','Team Image','Team','League','Value (Euro million)','Wage (Euro thousand)','Total Point']
SoFIFAdata = pd.DataFrame(columns = column)

Leagues = ["Premier League", "Bundesliga", "La Liga", "Serie A", "Ligue 1", "Others"]
Premier_League = ["Manchester City", "Chelsea", "Liverpool", "Manchester United", "Tottenham Hotspur", "Arsenal", "West Ham United", "Aston Villa", "Leicester City", "Newcastle United", "Wolverhampton Wanderers", "Everton", "Crystal Palace", "Leeds United", "Nottingham Forest", "Brighton & Hove Albion", "Fulham", "Southampton", "Brentford", "AFC Bournemouth"]
Bundesliga = ["FC Bayern München", "Borussia Dortmund", "RB Leipzig", "Bayer 04 Leverkusen", "Borussia Mönchengladbach", "Eintracht Frankfurt", "VfL Wolfsburg", "SC Freiburg", "TSG Hoffenheim", "FC Augsburg", "FSV Mainz 05", "FC Köln", "VfB Stuttgart", "FC Union Berlin", "Hertha BSC", "Schalke 04", "Werder Bremen", "VfL Bochum 1848"]
La_Liga = ["Real Madrid", "FC Barcelona", "Atlético Madrid", "Sevilla", "Villarreal", "Athletic Club", "Real Betis", "Real Sociedad", "Getafe", "Celta de Vigo", "Valencia", "Osasuna", "Rayo Vallecano", "Cádiz", "Espanyol", "Real Valladolid", "Almería", "Mallorca", "Elche", "Girona"]
Serie_A = ["Inter", "Juventus", "Milan", "Napoli", "Roma", "Atalanta", "Lazio", "Fiorentina", "Torino", "Udinese", "Sassuolo", "Bologna", "Monza", "Salernitana", "Sampdoria", "Hellas Verona", "Empoli", "Cremonese", "Lecce", "Spezia"]
Ligue_1 = ["Paris Saint Germain", "Olympique Marseille", "Olympique Lyonnais", "Monaco", "Nice", "Rennes", "Lens", "Lille", "Montpellier", "Nantes", "Strasbourg", "Brest", "Troyes", "Reims", "Angers SCO", "Toulouse", "Auxerre", "Ajaccio", "Lorient", "Clermont"]

Namelist = []

for offset in range(0,1000):
    SoFIFA_url = SoFIFA_url + str(offset)
    p_html = requests.get(SoFIFA_url)
    p_soup = p_html.text
    data = Soup(p_soup,'html.parser')
    table = data.find('tbody')
    for i in table.findAll('tr'):    
        td = i.findAll('td')
        picture = td[0].find('img').get('data-src')
        ID = int(td[0].find('img').get('id'))
        flag = td[1].find('img').get('data-src')
        Name = i.select_one(".col-name >a[aria-label]")["aria-label"]
        Age = int(int(td[2].text.split()[0]))
        Position = [p.get_text(strip=True) for p in i.select("span.pos")]
        Nationality = i.select_one("img.flag")["title"]
        Overall = int(td[3].find('span').text)
        Potential = int(td[4].find('span').text)
        Team_image = td[5].find('img').get('data-src')
        Team = td[5].find('a').text
        if Team == "":
            Team = "Free Player"
            Team_image = ""
        if Team in Premier_League:
            League = Leagues[0]
        elif Team in Bundesliga:
            League = Leagues[1]
        elif Team in La_Liga:
            League = Leagues[2]
        elif Team in Serie_A:
            League = Leagues[3]
        elif Team in Ligue_1:
            League = Leagues[4]
        else:
            League = Leagues[5]
        Value = td[6].text.strip()[1:]
        if Value[-1] == "M":
            Value = float(Value[:-1])
        elif Value == "0":
            Value = 0
        elif Value[-1] == "K":
            Value = float(Value[:-1])/1000

        Wage = td[7].text.strip()[1:]
        if Wage[-1] == "K":
            Wage = float(Wage[:-1])
        else:
            Wage = float(Wage)/1000
        
        Total_Point = int(td[8].text.strip())
        player_data = pd.DataFrame([[ID,picture,flag,Name,Age,Position,Nationality,Overall,Potential,Team_image,Team,League,Value,Wage,Total_Point]])
        #print(player_data)
        player_data.columns = column
        if Name not in Namelist:
            Namelist.append(Name)
            SoFIFAdata = SoFIFAdata.append(player_data, ignore_index = True)

print(SoFIFAdata.head()) 

SoFIFAdata.to_csv('SoFIFAdata.csv', index = None, encoding='utf-8-sig')

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8-sig') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8-sig') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'SoFIFAdata.csv'
jsonFilePath = r'SoFIFAdata.json'
csv_to_json(csvFilePath, jsonFilePath)

SRC_JSON = 'SoFIFAdata.json'
SRC = open(SRC_JSON, 'r', encoding='utf-8-sig')
SoFIFAdata = json.loads(SRC.read())
SRC.close()

for player in SoFIFAdata:
    player["ID"] = int(player["ID"])
    player["Age"] = int(player["Age"])
    player["Overall"] = int(player["Overall"])
    player["Potential"] = int(player["Potential"])
    player["Total Point"] = int(player["Total Point"])
    player["Value (Euro million)"] = float(player["Value (Euro million)"])
    player["Wage (Euro thousand)"] = float(player["Wage (Euro thousand)"])


with open("SoFIFAdata.json", "w") as fp:
    json.dump(SoFIFAdata, fp, indent=4)
 
fp.close()


# con = sqlite3.connect('SoFIFA.db')
