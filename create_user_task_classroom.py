from faker import Faker
import requests
from random import randint, choice

faker = Faker()


for i in range(100):
    response = requests.post(f'http://localhost:3000/tasks/add-user-task-classroom?taskClassroomId={randint(1, 9)}&userId={randint(12, 21)}')
    print(response.json())


