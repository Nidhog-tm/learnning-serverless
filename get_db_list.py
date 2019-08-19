import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('MT_serveres_test')

def get_person(id):
    response = table.scan()
    return response['Items']

def handler(event, context):
    person = get_person('001')
    return person
