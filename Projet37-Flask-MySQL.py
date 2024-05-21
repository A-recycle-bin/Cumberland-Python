# Script contenant les fonctions de base pour communiquer avec la db mysql

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

def change_something():
    cursor = mysql.connection.cursor()
    cursor.execute(" CREATE TABLE table_name(field1, field2...) ")
    cursor.execute(" INSERT INTO table_name VALUES(v1,v2...) ")
    cursor.execute(" DELETE FROM table_name WHERE condition ")
    mysql.connection.commit()
    cursor.close()
def select_everything():
    cursor = mysql.connection.connect()

    cursor.execute("SELECT * FROM name_of_table")
    DBData = cursor.fetchall()
    cursor.close()
    return DBData

    DBData = GetBookLink()
    return render_template("index.html", ScrapedBookData=DBData)