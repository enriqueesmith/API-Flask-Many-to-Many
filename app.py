import os, copy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Tag, Page
from flask_cors import CORS

app = Flask(__name__)
##Setting the place for the db to run
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/change_this_name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initializing the db (after registering the Models)
db.init_app(app)
#migration engine
migrate = Migrate(app, db)
# More code
CORS(app)

# Get a list of all the Contacts GET /contact/all
@app.route('/')
def hello():
    pages = Page.query.all()
    responseA =[]
    for p in pages:
        responseA.append(p.to_dict())
    tags = Tag.query.all()
    responseB =[]
    for t in tags:
        responseB.append(t.to_dict())
        
    return jsonify(responseA, responseB)

'''
# Contact
    id: (int, primary_key)
    full_name: (string, mandatory)
    email: (string, mandatory)
    address: (string, optional)
    phone: (string, optional)
    groups: (list of foreign_key)

# Group
    id: (int, primary_key)
    name: (string, mandatory)
    contacts: (list of foreign_key)
Formal API Documentation
'''

'''
#GET /contact/all
 
REQUEST (application/json)
    type: GET
    body: null
RESPONSE (application/json)
        code: 200 | 404 | 500
        body: [
            {
                "full_name": "Dave Bradley",
                "email": "dave@gmail.com",
                "address":"47568 NW 34ST, 33434 FL, USA",
                "phone":"7864445566",
                "groups": [2,3]
            },
            ...
        ]
# Create a new contact
    REQUEST (application/json)
        type: POST
        path: /contact
        body: {
            "full_name": "Dave Bradley",
            "email": "dave@gmail.com",
            "address":"47568 NW 34ST, 33434 FL, USA",
            "phone":"7864445566",
            "groups": [2,3]
        }
    RESPONSE (application/json)
        code: 200 | 400 | 500
        body: {
            "id": 12
            "full_name": "Dave Bradley",
            "email": "dave@gmail.com",
            "address":"47568 NW 34ST, 33434 FL, USA",
            "phone":"7864445566",
            "groups": [2,3]
        }
Get a specific Contact
    REQUEST (application/json)
        type: GET
        path: /contact/{contact_id}
    RESPONSE (application/json)
        code: 200 | 404 | 400 | 500
        body:{
            "id": 12
            "full_name": "Dave Bradley",
            "email": "dave@gmail.com",
            "address":"47568 NW 34ST, 33434 FL, USA",
            "phone":"7864445566",
            "groups": [
                {
                    "id": 2,
                    "name": "Family"
                },{
                    "id": 3,
                    "name": "Gamers"
                }
             ]
        }
Update a given contact
    REQUEST (application/json)
        type: PUT
        path: /contact/{contact_id}
        body: {
            "full_name": "Dave Bradley",
            "email": "dave@gmail.com",
            "address":"47568 NW 34ST, 33434 FL, USA",
            "phone":"7864445566",
            "groups": [2,3]
        }
    RESPONSE (application/json)
        code: 200 | 404 | 400 | 500
        body:{
            "id": 12
            "full_name": "Dave Bradley",
            "email": "dave@gmail.com",
            "address":"47568 NW 34ST, 33434 FL, USA",
            "phone":"7864445566",
            "groups": [2,3]
        }
Delete a contact by id
    REQUEST (application/json)
        type: DELETE
        path: /contact/{contact_id}
        body: null
    RESPONSE (application/json)
        code: 200 | 404 | 500
        body: {
            "deleted": {
                "id": 12,
                "full_name": "Dave Bradley",
            }
        }
List all Groups
    REQUEST (application/json)
        type: GET
        path: /group/
        body: null
    RESPONSE (application/json)
        code: 200 | 500
        body: {
            "data": [
                {
                    "id": 1,
                    "name": "Work"
                },{
                    "id": 2,
                    "name": "Gamers"
                }
            ]
        }
Get a specific Group
    REQUEST (application/json)
        type: GET
        path: /group/{group_id}
    RESPONSE (application/json)
        code: 200 | 404 | 400 | 500
        body:{
            "id": 2
            "name": "Work",
            "contacts": [
                {
                    "id": 12
                    "full_name": "Dave Bradley",
                    "email": "dave@gmail.com",
                    "address":"47568 NW 34ST, 33434 FL, USA",
                    "phone":"7864445566",
                    "groups": [2,3]
                }
             ]
        }
Update a given group's id
    REQUEST (application/json)
        type: PUT
        path: /group/{group_id}
        body: {
            "name": "Beach Crew",
        }
    RESPONSE (application/json)
        code: 200 | 404 | 400 | 500
        body:{
            "id": 2
            "name": "Beach Crew",
        }
Delete a group by id
    REQUEST (application/json)
        type: DELETE
        path: /group/{group_id}
        body: null
    RESPONSE (application/json)
        code: 200 | 404 | 500
        body: {
            "deleted": {
                "id": 2,
                "name": "Beach Crew",
            }
        }


# Add a Course     - /courses/add  -  POST    
@app.route('/courses/add', methods=['POST'])
def addCourses():
    info = request.get_json() or {}
    course = Course(name=info['name'])
    db.session.add(course)
    db.session.commit()
    return jsonify({'response': 'Ok'}) 
'''

  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))