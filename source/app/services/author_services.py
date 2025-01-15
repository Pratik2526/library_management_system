from source.app.config import Config,db 
from sqlalchemy import text

class AuthorService:

    def insert_author(data):

        name = data.get('name')

        with Config.engine.connect() as conn:
            trans = conn.begin()
            try:       
                query = text('INSERT INTO author (name) VALUES (:name)')
                conn.execute(query, {'name': name})
                trans.commit()            
                return {'message':'author added sucessfully'}
            except Exception as e:
                trans.rollback()
                return {'error': str(e)},400 
            
    def retrieve_authors(name=None):

        query = 'SELECT * FROM author'
        params = {}

        if name:
            query += ' WHERE name = :name'
            params['name'] = name 
        
        with Config.engine.connect() as conn:
            instance = conn.execute(text(query),params).fetchall()
            output = [{'id':row[0], 'name':row[1]} for row in instance]
            return output

            
    def update_author(id,data):

        set_clause = ', '.join([f'{key}= :{key}' for key in data.keys()])
        params = {key: value for key, value in data.items()}
        params['id'] = id
        query = f"UPDATE author SET {set_clause} WHERE id = :id"
        with Config.engine.connect() as conn:
            trans = conn.begin()
            try:
                conn.execute(text(query),params)
                trans.commit()
                return {'message':'author updated sucessfully'}
            except Exception as e:
                trans.rollback()
                return {'error': str(e)},400 
            
    def delete_author(id):

        query = 'DELETE FROM author WHERE id = :id'
        params = {'id':id} 

        with Config.engine.connect() as conn:
            trans = conn.begin()
            try:
                conn.execute(text(query),params)
                trans.commit()
                return {'message':'author deleted sucessfully'},204
            except Exception as e:
                trans.rollback()
                return {'error': str(e)},400 
