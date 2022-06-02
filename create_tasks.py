from faker import Faker
import requests
from random import randint, choice

faker = Faker()

teachers = [3, 4, 7, 11]

def create_task():
    data = {
        'name': faker.name(),
        'code': faker.random_number(digits=6),
        'description': faker.text(),
        'baseScore': randint(1, 10),
        'createdBy': choice(teachers),
    }
    return data


for i in range(10):
    data = create_task()
    response = requests.post('http://localhost:3000/tasks/create-task', json=data)
    print(response.status_code)



