from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

users = {
   'users_list' :
   [
      {
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123',
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222',
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'yat999',
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555',
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods= ['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      print("search name", search_username)
      print("search job", search_job)      
      if search_username and search_job:
         return find(search_username, search_job)
      elif search_username: 
         return find(search_username)
      return users 

   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd), 201
      return resp 

@app.route('/users/<id>', methods= ['GET', 'DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
         if user['id'] == id:
            if request.method == 'GET': 
               return user
         elif request.method == 'DELETE': 
            for user in users['users_list']:
               if user['id'] == id:
                  users['users_list'].remove(user)
                  id_string = "user id {} deleted".format(id)
                  resp = jsonify({"success":id_string}), 204
                  return resp 

      resp = jsonify({"Msg": "User not found"}), 404
      return resp 
   return users

def find(name=None, job=None): 
   subdict = {'users_list':[]}
   for user in users['users_list']: 
      if user['name'] == name and user['job'] == job: 
         subdict['users_list'].append(user)
   return subdict 


