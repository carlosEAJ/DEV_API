from flask_restful import Resource

habilidades = ['Python', 'Java', 'C#', 'PHP', 'JavaScript']
class Habilidades(Resource):
    def get(self):
        return habilidades