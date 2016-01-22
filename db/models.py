import json
from app import db

'''
   data struncture:
    [{
     name: 
     type: system or algorithm
     limit: 
     weigth:
     components:[{  #only if type system
         ...
       },]
     },]
    '''


class System(db.Model):

    __tablename__ = 'system'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(1024), unique=True)
    data = db.Column(db.Text)
    
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = json.dumps(data)

    def getData(self):
        return json.loads(self.data)

    def __repr__(self):
        return '<System %r>' % (self.name)

