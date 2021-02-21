import psycopg2
import json

import config as cfg

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

conn = None
cur = None 

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
    return json.dumps(lst)

class Book(Resource):
    def get(self, book_id):

        cur.execute('select json_agg(to_json(d)) from ( select b.name, pg.page_number, pg.text from book b inner join page pg on pg.book_id = b.book_id and b.book_id = {id} ) as d'.format(id = book_id))
    
        book_data = cur.fetchone()[0]
        book_data = toJSON(book_data)
        print(book_data)

        return book_data

class Object(Resource):
    def get(self, page_id):

        cur.execute('select json_agg(to_json(d)) from ( select o.texture, o.transform_x, o.transform_y, o.animation_id from object o inner join page pg on pg.page_id = o.page_id and o.page_id = {id} ) as d'.format(id = page_id))

        object_data = cur.fetchone()[0]
        object_data = toJSON(object_data)
        print(object_data)

        return object_data

api.add_resource(Book, "/book/<int:book_id>")
api.add_resource(Object, "/object/<int:page_id>")

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
    
    app.run()

	# close the communication with the PostgreSQL
    cur.close()

    if conn is not None:
                conn.close()
                print('Database connection closed.')