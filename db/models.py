import json
from app import db

'''
   data struncture:
    [{
     name:
     type: system or algorithm
     limit:
     weigth:
     input:
     output:
     weigth:
     next: { ... # next system to call }
     components:[{  #only if type system
         ...
       },]
     },]
    '''

class SystemDao(db.Model):

    __tablename__ = 'system'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(1024), unique=True)
    data = db.Column(db.Text)

    def __init__(self, name=None, data=None):
        self.name = name
        self.data = json.dumps(data)

    def get_components(self):
        data = json.loads(self.data)
        ret = []
        for i in data:
            ret.append(self, self._get_subcomponents(i))

    def _get_subcomponents(self, data):
        ret = []
        for i in data:
            s = System(
                    data['name'],
                    data['type'],
                    data['limit'],
                    self._get_subcomponents(data['components'])
                )
            ret.append(s)
        return ret


