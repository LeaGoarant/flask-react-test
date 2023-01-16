from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/request": {"origins": "*"}})

@app.route('/request')
def proxy():
    return Response('Hello', status=200)

app.run(host='0.0.0.0', port=8000)
