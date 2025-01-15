from flask.views import MethodView 
from flask import request,jsonify
from source.app.services.author_services import AuthorService

class RetrieveInsertAuthor(MethodView):

    def post(self):
        try:
            data = request.json 
            output = AuthorService.insert_author(data)
            return output
        except Exception as e:
            return jsonify({'error': str(e)}), 400 
        
    def get(self):
        try:
            name = request.args.get('name')
            print('name',name)
            output = AuthorService.retrieve_authors(name)
            return jsonify(output)
        except Exception as e:
            return jsonify({'error': str(e)}), 400 
        
    def put(self,id):
        try:
            data = request.json
            output = AuthorService.update_author(id,data)
            return jsonify(output)
        except Exception as e:
            return jsonify({'error': str(e)}), 400 

    def delete(self,id):
        try:
            output = AuthorService.delete_author(id)
            return jsonify(output) 
        except Exception as e:
            return jsonify({'error': str(e)}), 400 