import json
from src import system
from webserver import db

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

    __tablename__ = 'systemdao'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(1024), unique=True)
    data = db.Column(db.Text)

    def __init__(self, name=None, data=None):
        self.name = name
        self.data = json.dumps(data)

    def get_system(self):
        data = json.loads(self.data)
        return self._get_system(data)

    def _get_system(self, data):
        next_system = None
        components = []
        for i in data['components']:
            components.append(self._get_system(i))
        if data['next_s']:
            next_system = self._get_system(data['next_s'])

        return system.System(data['name'], data['s_type'], data['limit'],
            data['weight'], data['input_type'], data['output_type'], components, next_system)


