from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
      },
      {
         'id' : 'zap888',
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])

def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')

      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if ((user['name'] == search_username) and (user['job'] == search_job)): 
               subdict['users_list'].append(user)
         return subdict 
      return users  

   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

   elif request.method == 'DELETE': 
      userToDelete = request.get_json() #expecting this to be a full JSON of the user 
      userlist = users.get('users_list')  
      for user in userlist: 
         if user ==  userToDelete: 
            userlist.remove(user)
      return users




