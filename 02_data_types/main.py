from pydantic  import ValidationError
import requests 
from models import Student

url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()
for student in data:
    try:
        main=Student(**student)
        print(main)
        break
    except ValidationError as e:
            print(e)


   
