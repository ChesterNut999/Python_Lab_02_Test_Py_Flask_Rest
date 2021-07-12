from flask_restful import Resource

dev_habilidades = ['Python', 'Java', 'C++', 'Ruby', 'Maven', 'Flask']

class Dev_Habilidades(Resource):
    def get(self):
        return dev_habilidades