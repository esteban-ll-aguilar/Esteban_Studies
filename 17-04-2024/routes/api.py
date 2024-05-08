from flask import Blueprint, jsonify, make_response, request
from controls.personaDaoControl import PersonaDaoControl
api = Blueprint('api', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion

@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code": 200}),
        200
    )

@api.route('/api/personas')
def lista_personas():
    pd = PersonaDaoControl()
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data":pd.to_dict() }),
        200
    )