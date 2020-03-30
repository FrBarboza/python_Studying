from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def pessoa():
    return jsonify({'nome': 'Fernando'})


if __name__ == '__main__':
    app.run(debug=True)
