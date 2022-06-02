from faker import Faker
import requests
from random import randint

faker = Faker()


def create_user():
    name = faker.name().split(' ')
    data = {
        'names': name[0],
        'lastNames': name[1],
        'email': faker.email(),
        'password': faker.password(),
        'dni': faker.random_number(digits=8),
        'dniTypeId': randint(1, 3),
        'roleId': randint(1, 3),
        'birthDate': str(faker.date_of_birth(tzinfo=None, minimum_age=8, maximum_age=18)),
        'city': faker.city(),
        'country': faker.country(),
    }
    return data


for i in range(10):
    data = create_user()
    response = requests.post('http://localhost:3000/auth/register', json=data)
    print(response.status_code)



