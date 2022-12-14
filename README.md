# SI507-Final-Project
This project allows you to get a list of recommended players based on your preference in a Flask Web App.

## Data Sources
SoFIFA: https://sofifa.com/

Player data: https://sofifa.com/players

Club data: https://sofifa.com/teams?type=club

National team data: https://sofifa.com/teams?type=national  and  https://www.fifa.com/fifa-world-ranking/men 


## How to run
1. install all requirements with `pip install -r requirements.txt`
2. download templates file, SoFIFA.db, and app.py
3. then you should run with `python app.py runserver`
4. follow the Flask app routes (http://127.0.0.1:5000/) to get to each page. 

## How to use
1. In the `/home` page, you can first select players by leagues, then sort them by their age, overall rating, potential, market value, wage, or total point, and lastly you need to determine the sort order. 
2. then it will take you to the `/results` page, show 5 players that satisfy your request. 
3. besides, you can also choose to see the graph rather than the table. It will show you the bar chart.

## Routes in this app
- `/` and `/home`: the index
- `/results`: the results
- `/about`: it will take you to the github page of this project
- `/datasource`: it will take you to the SoFIFA offical site. 

## Project Demo
https://www.bilibili.com/video/BV1aV4y1w762/?spm_id_from=333.999.0.0

https://www.bilibili.com/video/BV1kP4y1D7iW/?spm_id_from=333.999.0.0&vd_source=1f424fe28fe5672fb5f63ea4f5d8e0eb


# Appreciate. 
