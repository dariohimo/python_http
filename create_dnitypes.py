import requests

dni_types = ["cc", "ce", "pa"]

def create_dnitype(dni_type):
    data = {
        'name': dni_type
    }
    response = requests.post('http://localhost:3000/utils/create-dnitype', json=data)
    print(response.status_code)


for dni_type in dni_types:
    create_dnitype(dni_type)