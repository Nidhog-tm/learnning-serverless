import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('MT_serveres_test')

def get_person(id):
    response = table.scan()
    return response['Items']

def handler(event, context):
    person = get_person('001')
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': person
        })
    }
