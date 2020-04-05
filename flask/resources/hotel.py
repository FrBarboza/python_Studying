from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3


# path / hoteis?cidade=Rio de Janeiro&estrelas_min=4&diaria_max=400
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)


def normalize_path_params(cidade=None,
                          estrelas_min = 0,
                          estrelas_max = 5,
                          diaria_min = 0,
                          diaria_max = 10000,
                          limit = 50,
                          offset = 0,
                          **data):
    if cidade:
        return {
            'cidade': cidade,
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'limit': limit,
            'offset': offset
        }
    return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset
    }

# class Hoteis(Resource):
#     def get(self):
#         return {'hoteis': hoteis}

class Hoteis(Resource):
    def get(self):
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        value_data = path_params.parse_args()
        # dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        valid_data = {key:value_data[key] for key in value_data if value_data[key] is not None}
        parameters = normalize_path_params(**valid_data)

        if not parameters.get('cidade'):
            query = "SELECT * FROM hoteis \
            WHERE (estrelas >= ? AND estrelas <= ?) \
            AND (diaria >= ? AND diaria <= ?) LIMIT ? OFFSET ?"

            values = tuple([parameters[key] for key in parameters])
            result = cursor.execute(query, values)
        else:
            query = "SELECT * FROM hoteis \
            WHERE (cidade = ?) \
            AND (estrelas >= ? AND estrelas <= ?) \
            AND (diaria >= ? AND diaria <= ?) LIMIT ? OFFSET ?"

            values = tuple([parameters[key] for key in parameters])
            result = cursor.execute(query, values)
    	
        hoteis = []
        for hotel in result:
            hoteis.append({
            'hotel_id': hotel[0],
            'nome': hotel[1],
            'estrelas': hotel[2],
            'diaria': hotel[3],
            'cidade': hotel[4]
        })

        return {'hoteis': hoteis}
        # é um Select * from hoteis
        #return {'hoteis': [hoteis.json() for hoteis in HotelModel.query.all()]}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' is required.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas is required.'" )
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'Erro: ': 'Hotel não encontrado na lista'}, 404

    @jwt_required
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'Message':'Hotel {} already exists.'.format(hotel_id)}, 400
        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except (ValueError, Exception):
            return {'message':'An internal error occured trying to save hotel'}, 500 # Internal error server
        return hotel.json(), 201

    @jwt_required
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            hotel_found.update_hotel(**dados)
            hotel_found.save_hotel()
            return hotel_found.json(), 200
        
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except (ValueError, Exception):
            return {'message': 'An internal error occurred trying to save hotel'}, 500  # Internal error server
        return hotel.json(), 201

    @jwt_required
    def delete(self, hotel_id):
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            try:
                hotel_found.delete_hotel()
            except (ValueError, Exception):
                return {'message': 'An internal error occurred trying to delete hotel'}, 500 # Internal error server
            return {'message': 'Hotel deleted'}
        return {'message': 'Hotel not found.'}, 404
