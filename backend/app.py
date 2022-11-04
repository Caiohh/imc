from flask import request  # recebe informações do usuário
from flask import jsonify  # transforma dicionário em json
from flask import Flask  # nosso app

app = Flask(__name__)  # cria o app

@app.route('/api', methods = ['POST'])  # enpoint da api
def calcula_imc():
    resp = request.get_json()  # pega informação do usuário
    peso, altura = resp ["peso"], resp["altura"]  # desempacota informação
    resultado = round(peso / altura ** 2, 2)  # calcula imc
    return jsonify({"resultado": resultado})  #retorna resultado em json

@app.after_request  # permite requisição de outros servidores
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type,Authorization")
    return response

if __name__=="__main__":
    app.run()  # roda o app em http://127.0.0.1:5000