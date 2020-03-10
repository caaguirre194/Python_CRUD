import requests
from connection import connection
from b64 import decode, encode
from properties import getConfig


def request(token):
    properties = getConfig()
    url = properties['ENDPOINT']['endpoint_request']

    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json; UTF-8', }

    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print("Ocurrió un error al realizar la petición: ", e)

    if response.status_code == 200:
        payload = response.json()
        print("=> Request correcta")
        return payload
    else:
        print("=> Request incorrecta")
        return None


def login(offset=0):
    properties = getConfig()
    url = properties['ENDPOINT']['endpoint_auth']

    myobj = {'email': encode(properties['USER']['username']), 'password': encode(
        properties['USER']['password'])}

    args = {
        "Content-Type": "application/json;"
    } if offset else {}

    try:
        response = requests.post(url, json=myobj, params=args)
    except Exception as e:
        print("Ocurrió un error al realizar la Autenticación: ", e)

    if response.status_code == 200:
        payload = response.json()
        print("=> Autenticación correcta")
        print(payload)
        return payload.get('token')
    else:
        print("=> Autenticación incorrecta")
        return None


def saveUser(id, nombres, apellidos, genero, anios):
    try:
        with connection.cursor() as cursor:
            consulta = "INSERT INTO testuser(id,nombres,apellidos,genero,anios) VALUES (?,?,?,?,?);"
            cursor.execute(consulta, id, nombres, apellidos, genero, anios)
            print("=> Usuario guardado correctamente")
    except Exception as e:
        print("=> Ocurrió un error al insertar el usuario: ", e)


if __name__ == '__main__':
    token = login()
    if token != None:
        request = request(token)
        if request != None:
            print(request[0])
            saveUser(request[0].get('id'), request[0].get('nombres'),
                     request[0].get('apellidos'), request[0].get('genero'), request[0].get('anios'))
