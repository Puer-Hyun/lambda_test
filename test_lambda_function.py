import json
from lambda_function import lambda_handler

with open('example_event.json') as f:
    event = json.load(f)

context = {}

# lambda_handler 함수를 호출하고 결과를 출력합니다.
response = lambda_handler(event, context)
print(response)
