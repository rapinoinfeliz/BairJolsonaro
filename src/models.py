from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from datetime import datetime

db_connect = create_engine('sqlite:///bairjolsonaro.db')
app = Flask(__name__)

# Tag:
# - tag_id
# - name
# - created_at
# - updated_at
class Tags(Resource):

    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from tags")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        name = request.json['name']
        
        created_at = datetime.date.today()
        updated_at = datetime.date.today()

        conn.execute(
            "insert into tags values(null, '{0}','{1}', '{2}')".format(name, created_at, updated_at))

        query = conn.execute('select * from tags order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        
        id = request.json['id']

        # Attribute: name
        if ((request.json['name']) and (request.json['name']!='') ):
            name = request.json['name']
        else:
            name = None

        # Attribute: update_at
        if ((request.json['update_at']) and (request.json['update_at']!='') ):
            update_at = request.json['update_at']
        else:
            update_at = datetime.date.today()

        conn.execute("update tags set name ='" + str(name) +
                     "', updated_at ='" + str(updated_at) + "' 
                     where id =%d " % int(id))

        query = conn.execute("select * from tags where id=%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


# Quote:
# - quote_id (PK)
# - content
# - author_id
# - source_url
# - created_at
# - updated_at
class Quotes(Resource):

    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from quotes")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        content = request.json['content']
        
        author_id = request.json['author_id']
        source_url = request.json['source_url']
        
        created_at = datetime.date.today()
        updated_at = datetime.date.today()

        conn.execute(
            "insert into quotes values(null, '{0}','{1}', '{2}', '{3}', '{4}')".format(content, author_id, source_url, created_at, updated_at))

        query = conn.execute('select * from quotes order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        
        id = request.json['id']

        if ((request.json['content']) and (request.json['content']!='') ):
            content = request.json['content']
        else:
            content = None
        
        if ((request.json['author_id']) and (request.json['author_id']!='') ):
            author_id = request.json['author_id']
        else:
            author_id = None

        # Attribute: source_url
        if ((request.json['source_url']) and (request.json['source_url']!='') ):
            source_url = request.json['source_url']
        else:
            source_url = None
        
        # # Attribute: created_at
        # if ((request.json['created_at']) and (request.json['created_at']!='') ):
        #     created_at = request.json['created_at']
        # else:
        #     created_at = None

        # Attribute: update_at
        if ((request.json['update_at']) and (request.json['update_at']!='') ):
            update_at = request.json['update_at']
        else:
            update_at = datetime.date.today()

        conn.execute("update quotes set content ='" + str(content) +
                     "', updated_at ='" + str(updated_at) + "'  
                     "', source_url ='" + str(source_url) + "'
                     "', author_id ='" + str(author_id) + "'
                     where id =%d " % int(id))

        query = conn.execute("select * from quotes where id=%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

# class Users(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select * from user")
#         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
#         return jsonify(result)

#     def post(self):
#         conn = db_connect.connect()
#         name = request.json['name']
#         email = request.json['email']

#         conn.execute(
#             "insert into user values(null, '{0}','{1}')".format(name, email))

#         query = conn.execute('select * from user order by id desc limit 1')
#         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
#         return jsonify(result)

#     def put(self):
#         conn = db_connect.connect()
#         id = request.json['id']
#         name = request.json['name']
#         email = request.json['email']

#         conn.execute("update user set name ='" + str(name) +
#                      "', email ='" + str(email) + "'  where id =%d " % int(id))

#         query = conn.execute("select * from user where id=%d " % int(id))
#         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
#         return jsonify(result)

# class UserById(Resource):
#     def delete(self, id):
#         conn = db_connect.connect()
#         conn.execute("delete from user where id=%d " % int(id))
#         return {"status": "success"}

#     def get(self, id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from user where id =%d " % int(id))
#         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
#         return jsonify(result)