from flask import Blueprint, jsonify, make_response, request
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
api = Blueprint('api', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
CORS(api)
cors = CORS(api, resources={
    r"/*": {
        "origins": "*"
        }
    })


@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code": 200}),
        200
    )
# LISTA PERSONA GET
@api.route('/api/personas')
def lista_personas():
    pd = PersonaDaoControl()
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data":pd.to_dict() }),
        200
    )
# GUARDAR PERSONA POST
@api.route('/api/personas/guardar', methods=['POST'])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.json
    print(type(data))
    if "apellidos" not in data:
        return make_response(
            jsonify({"msg":"Falta apellidos", "code": 400, data: []}),
            400
        )
    #TODO validar
    pd._persona._nombre = data['nombre']
    pd._persona._apellidos = data['apellidos']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['telefono']
    pd._persona._direccion = data['direccion']
    pd._persona._tipoIdentificacion = data['tipoIdentificacion']
    pd.save
    return make_response(
        jsonify({"msg":"OK, la persona se ha agregado correctamente", "code": 200, "data":[] }),
        200
    )