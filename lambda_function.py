import json

def lambda_handler(event, context):
    left = event["left"]
    right = event["right"]
    result = (left ** right) + 10
    
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