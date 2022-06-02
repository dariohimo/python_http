from faker import Faker
import requests
from random import randint, choice

faker = Faker()

teachers = [3, 4, 7, 11]

def create_taskClassroom():
    data = {
        'taskId': randint(1, 10),
        'classroomId': randint(1, 13),
    }
    return data


for i in range(10):
    response = requests.post(f'http://localhost:3000/classrooms/add-task?taskId={randint(1, 10)}&classroomId={randint(1, 13)}')
    print(response.status_code)


