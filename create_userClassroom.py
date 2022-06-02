import requests
from random import randint

def create_userClassroom():
    response = requests.post(f'http://localhost:3000/classrooms/add-teacher?classroomId={randint(1,13)}&teacherId={randint(1,21)}')
    print(response.status_code)

for i in range(20):
    create_userClassroom()