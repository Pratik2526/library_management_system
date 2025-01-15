from flask import Blueprint
from source.app.controllers.author_controller import RetrieveInsertAuthor

author_bp = Blueprint('author_bp',__name__)

author_bp.add_url_rule('/api/author',view_func=RetrieveInsertAuthor.as_view('retrieve-insert-author'),methods=['POST','GET'])
author_bp.add_url_rule('/api/author/<int:id>',view_func=RetrieveInsertAuthor.as_view('update-delete-author'),methods=['PUT','DELETE'])