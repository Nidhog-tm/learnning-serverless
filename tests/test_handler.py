import unittest
import json
import hello
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello World', result['body'])
        
        event = {'pathParameters': {'name': 'Takashi'} }
        result = hello.handler(event, None)
        print(result) 
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('hello Takashi', result['body'])
        


if __name__ == '__main__':
    unittest.main()
