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
        hotel_found = Hotel.find_hotel(self, hotel_id)
        if hotel_found:
            return hotel_found
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
        hotel_object = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_object.json()
        hotel_found = Hotel.find_hotel(self, hotel_id)
        if hotel_found:
            hotel_found.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'Message: ': 'Hotel removido'}, 200
