
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_results(League, sort_by, sort_direction):
    conn = sqlite3.connect('SoFIFA.db')
    cur = conn.cursor()

    if sort_by == 'Age':
        sort_column = 'Age'
    elif sort_by == 'Overall Rating':
        sort_column = 'S.Overall'
    elif sort_by == 'Potential Rating':
        sort_column = 'Potential'
    elif sort_by == 'Market Value':
        sort_column = '"Value (Euro million)"'
    elif sort_by == 'Wage':
        sort_column = '"Wage (Euro thousand)"'
    else:
        sort_column = '"Total Point"'

    where_clause = ''
    if (League != 'All'):
        where_clause = f'where L.League = "{League}"'

    q = f'''
        select S.ID, S.Name, S.Age, S.Position, S.Overall, S.Potential, S."Value (Euro million)",
                S."Wage (Euro thousand)", S."Total Point", T.Team, N.Nation
            from SoFIFAdata as S join Teamdata as T on S."Team Id" = T.ID
            join Leagues L on T."League Id" = L.ID
            join Nationdata N on S."Nation Id" = N.ID   
            {where_clause}
            ORDER BY {sort_column} {sort_direction}
            LIMIT 5
    '''
    print(q)
    results = cur.execute(q).fetchall()
    conn.close()
    print(results)
    return results
    
@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return redirect("https://github.com/DengXiangyun/SI507-Final-Project")

@app.route("/datasource")
def datasource():
    return redirect("https://sofifa.com/")

@app.route('/results', methods=['POST'])

def players():
    League = request.form['League']
    sort_by = request.form['sort']
    sort_direction = request.form['dir']

    results = get_results(League, sort_by, sort_direction)

    return render_template('results.html', 
            sort=sort_by, results=results)


if __name__ == '__main__':
    app.run(debug=True)
    
    



    
