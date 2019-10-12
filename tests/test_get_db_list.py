import json
import unittest
from moto import mock_dynamodb2
import boto3
import get_db_list as app


class create_db:
    """
    mockデータベース、テストデータ作成クラス
    """
    @staticmethod
    def create_db_insert_data():
        dynamodb = boto3.resource('dynamodb')
        dynamodb.create_table(
            TableName='MT_serveres_test',
            KeySchema=[
                {
                    'AttributeName': 'test_id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'test_id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 50
            }
        )
        table = dynamodb.Table('MT_serveres_test')

        table.put_item(Item={
            'test_id': '001',
            'name': 'matsuoka'
        })

        table.put_item(Item={
            'test_id': '002',
            'name': 'awaji'
        })


class TestHandlerCase(unittest.TestCase):

    @mock_dynamodb2
    def setUp(self):
        self.create = create_db

    def tearDown(self):
        pass

    def test_lambda_handler(self):
        pass

    @mock_dynamodb2
    def test_200_ok(self):
        self.create.create_db_insert_data()
        apigw_event = ""
        anti_result = {'result':
                           [
                               {'test_id': '001', 'name': 'matsuoka'},
                               {'test_id': '002', 'name': 'awaji'}
                            ]
                       }
        ret = app.handler(apigw_event, "")
        data = json.loads(ret['body'])
        assert ret['statusCode'] == 200
        assert anti_result == data


if __name__ == "__main__":
    unittest.main()
