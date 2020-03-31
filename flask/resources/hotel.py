from flask_restful import Resource, reqparse
from models.models import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'Erro: ': 'Hotel não encontrado na lista'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'Message':'Hotel {} already exists.'.format(hotel_id)}, 400
        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            hotel_found.update_hotel(**dados)
            hotel_found.save_hotel()
            return hotel_found.json(), 200
        
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, hotel_id):
        global hoteis
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            hotel_found.delete_hotel()
            return {'Message: ': 'Hotel deleted'}
        return {'message':'Hotel not found.'}, 404
