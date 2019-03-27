from flask_sqlalchemy import SQLAlchemy
  
db = SQLAlchemy()


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))
        
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


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return "{'id': %s }" % self.id
    
    def to_dict(self):
        return {
            "id": self.id
        }
    
    
    