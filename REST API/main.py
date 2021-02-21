import psycopg2
import json

import config as cfg

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def connect():
    """ Connect to the PostgreSQL database server """
    connection = None

    try:        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(
            host=cfg.cfg['host'],
            database=cfg.cfg['database'],
            user=cfg.cfg['user'],
            password=cfg.cfg['password'],
        )

        return connection

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
def toJSON(lst):
    return json.dumps(dict(lst))

class Book(Resource):
    def get(self, book_id):
        return {"book_data" : "Hello World"}

api.add_resource(Book, "/book/<int:book_id>")

if __name__ == "__main__":
		
    #establish connection
    conn = connect()
    # create a cursor
    cur = conn.cursor()

	# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchall()
    print(db_version)
    
    app.run(debug=True)

	# close the communication with the PostgreSQL
    cur.close()

    if conn is not None:
                conn.close()
                print('Database connection closed.')