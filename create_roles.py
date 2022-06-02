import requests

roles = ["admin", "teacher", "student"]

def create_role(role):
    data = {
        'name': role
    }
    response = requests.post('http://localhost:3000/utils/create-role', json=data)
    print(response.status_code)


for role in roles:
    create_role(role)