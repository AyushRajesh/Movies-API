from flask import Flask, request, jsonify
import pymysql
import json

app=Flask(__name__)

def db_connection():
    conn=None
    try:
        conn=pymysql.connect(
            host= 'localhost',
            database= 'test',
            user= 'root',
            password= '',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn


@app.route('/movies', methods=['GET','POST'])
def movies():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method=='GET':
        cursor.execute("SELECT * FROM movies")
        movies=[
            dict(id=row['id'], Name=row['Name'], Actor=row['Actor'], Actress=row['Actress'], Year=row['Year'], Director=row['Director'])
            for row in cursor.fetchall()
        ]
        if movies is not None:
            return jsonify(movies)
       
    if request.method=='POST':
        new_Name=request.form['Name']
        new_Actor=request.form['Actor']
        new_Actress=request.form['Actress']
        new_Year=request.form['Year']
        new_Director=request.form['Director']
        cursor.execute("INSERT INTO movies (Name, Actor, Actress, Year, Director) VALUES(%s, %s, %s, %s, %s)", (new_Name, new_Actor, new_Actress, new_Year, new_Director,))
        conn.commit()
        return "Movie details created successfully"

@app.route('/movie/<int:id>', methods=['GET','PUT','DELETE'])
def single_movie(id):
    conn=db_connection()
    cursor=conn.cursor()
    movie=None
    if request.method=='GET':
       
       cursor.execute("SELECT * FROM movies WHERE id=%s",(id,))
       rows=cursor.fetchall()
       for r in rows:
           movie=r
       if movie is not None:
           return jsonify(movie), 200
       else:
           return "No Movie found for this id.", 404

    if request.method=='PUT':
        try:
         
            Name=request.form['Name']
            Actor=request.form['Actor']
            Actress=request.form['Actress']
            Year=request.form['Year']
            Director=request.form['Director']

            cursor.execute("UPDATE movies SET Name=%s, Actor=%s, Actress=%s, Year=%s, Director=%s WHERE id=%s",(Name, Actor, Actress, Year, Director, id,))
            conn.commit()
            updated_movie = {
                'id': id,
                'Name': movie['Name'],
                'Actor': movie['Actor'],
                'Actress': movie['Actress'],
                'Year': movie['Year'],
                'Director': movie['Director']
            }
        except:
            return "Movie with id {} has been updated successfully".format(id)
            return jsonify(updated_movie)
    if request.method=='DELETE':
        sql="""DELETE FROM movies WHERE id=%s"""
        cursor.execute(sql,(id))
        conn.commit()
        return "The movie with id: {} has been deleted.".format(id), 200
     
if __name__=='__main__':
    app.run(debug=True)
