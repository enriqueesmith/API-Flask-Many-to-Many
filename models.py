from flask_sqlalchemy import SQLAlchemy
  
db = SQLAlchemy()

'''
    "name": String,
	"email": String,
	"phone": String,
	"address": String,
'''


contacts = db.Table('contacts',
    db.Column('contact_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    contacts = db.relationship('Contact', secondary=contacts, lazy='subquery',
        backref=db.backref('groups', lazy=True))
        
    def __repr__(self):
        return 'Page: %s' % (self.name)
        
    def to_dict(self):
        
        tags = []
        for t in self.tags:
            tags.append(t.to_dict())
        
        return {
            "id": self.id,
            "tags": tags
        }


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    
    def __repr__(self):
        return "{'id': %s }" % self.id
    
    def to_dict(self):
        return {
            "id": self.id
        }
    
    
    