# CREATE CLASSES
## Player Class
class player():
    def __init__(self, json):
        self.name = json["Name"]
        self.id = json["ID"]
        self.playerid = json["PlayerId"]
        self.photo = json["picture"]
        self.age = json["Age"]
        self.position = json["Position"]
        self.overall = json["Overall"]
        self.potential = json["Potential"]
        self.value = json["Value"]
        self.wage = json["Wage"]
        self.point= json["Total_Point"]
        self.teamid = json["TeamId"]
        self.nationid = json["NationId"]

## Club Class
class team():
    def __init__(self,json):
        self.name = json["Team"]
        self.id = json["ID"]
        self.flag = json["Team_Image"]
        self.leagueid = json["LeagueID"]
        self.overall = json["Overall"]

## League Class
class league():
    def __init__(self,json):
        self.id = json["ID"]
        self.name = json["Name"]

## National Team Class
class nation():
    def __init__(self,json):
        self.name = json["Nation"]
        self.id = json["ID"]
        self.flag = json["Nation Image"]
        self.ranking = json["Ranking"]


