import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MT_serveres_test')

def handler(event, context):
    print(event)
    table.put_item(
        Item = {
            'test_id': event['test_id'],
            'name': event['name']
        }
    )
    print("PutItem succeeded:")