from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required


# class Hoteis(Resource):
#     def get(self):
#         return {'hoteis': hoteis}

class Hoteis(Resource):
    def get(self):
        # é um Select * from hoteis
        return {'hoteis': [hoteis.json() for hoteis in HotelModel.query.all()]}

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
