import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MT_serveres_test')


def get_person():
    response = table.scan()
    return response['Items']


def handler(event, context):
    person = get_person()
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            'Access-Control-Allow-Methods': 'OPTIONS,POST',
        },
        'body': json.dumps({
            'result': person
        }, ensure_ascii=False)
    }
