import json

def handler(event, context):
  data = {
    'output': 'my name is ' + event["pathParameters"]["name"]
  }
  return {'statusCode': 200,
    'body': json.dumps(data),
    'headers': {'Content-Type': 'application/json'}}
