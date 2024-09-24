import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    left = body["left"]
    right = body["right"]
    result = left ** right + 100
    
    print(f"left: {left}")
    print(f"right: {right}")
    print(f"result: {result}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda!',
            'result': result
        })
    }