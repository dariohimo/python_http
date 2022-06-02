from faker import Faker
import requests
from random import randint

faker = Faker()


def create_classroom():
    data = {
        'name': faker.name(),
        'capacity': randint(10, 30),
        'code': faker.random_number(digits=6),
        'adminDescription': faker.text(),
        'description': faker.text(),
        'endsAt': str(faker.date_time_between(start_date="now", end_date="+180d")),
        'createdBy': 5,
    }
    return data


for i in range(randint(1, 5)):
    data = create_classroom()
    response = requests.post('http://localhost:3000/classrooms/create-classroom', json=data)
    print(response.status_code)



