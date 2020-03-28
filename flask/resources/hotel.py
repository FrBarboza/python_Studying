from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 3.8,
        'diaria': 220.34,
        'cidade': 'Ria Claro'
    },
    {
        'hotel_id': 'gama',
        'nome': 'Gama Hotel',
        'estrelas': 4.5,
        'diaria': 380.34,
        'cidade': 'Piracicaba'
    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel_found = Hotel.find_hotel(self, hotel_id)
        if hotel_found:
            return hotel_found
        return {'Erro: ': 'Hotel não encontrado na lista'}, 404

    def post(self, hotel_id):
        
        dados = Hotel.argumentos.parse_args()

        # novo_hotel = {
        #     'hotel_id': hotel_id,
        #     'nome': dados['nome'],
        #     'estrelas': dados['estrelas'],
        #     'diaria': dados['diaria'],
        #     'cidade': dados['cidade']
        # }
        
        hotel_found = Hotel.find_hotel(self, hotel_id)
        if hotel_found:
            return {'Message: ': 'Hotel já inserido na lista!'}, 203

        novo_hotel = {'hotel_id': hotel_id, **dados}
        hoteis.append(novo_hotel)
        

        message = {'Mensagem: ': 'Hotel inserido com sucesso!'}
        message.update(novo_hotel)

        return message, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}

        hotel_found = Hotel.find_hotel(self, hotel_id)
        if hotel_found:
            hotel_found.update(novo_hotel)
            return novo_hotel
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        # dados = Hotel.argumentos.parse_args()
        # remove_hotel = {'hotel_id': hotel_id, **dados}

        hotel_found = Hotel.find_hotel(self, hotel_id)
       
        #message = {'Mensagem: ': 'Hotel removido com sucesso!'}
        #message.update(remove_hotel)

        if hotel_found:
            hoteis.remove(hotel_id)
            return {'Message: ': 'Removido'}, 200
        return {'Erro: ': 'Hotel não encontrado na lista'}, 404