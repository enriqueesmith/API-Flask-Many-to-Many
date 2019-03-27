import os, copy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Tag, Page

app = Flask(__name__)
##Setting the place for the db to run
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/change_this_name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initializing the db (after registering the Models)
db.init_app(app)
#migration engine
migrate = Migrate(app, db)

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

# Create a new Contact POST /contact


# Get a specific Contact (with the Group objects it belongs to) GET /contact/{contact_id}
# Delete a Contact DELETE /contact/{contact_id}
# Update a Contact UPDATE /contact/{contact_id}
# Get a list of all the Group names and ids GET /group/all
# Get a specific Group (with all Contact objects related to it) GET /group/{group_id}
# Update a Group name UPDATE /group/{group_id}
# Delete a Group DELETE /group/{group_id}

'''
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