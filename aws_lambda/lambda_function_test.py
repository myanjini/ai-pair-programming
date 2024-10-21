import unittest
import json
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):
        # Simulate S3 event
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {
                            'name': 'my-test-bucket'
                        },
                        'object': {
                            'key': 'test-object.txt'
                        }
                    }
                }
            ]
        }
        
        # Call the lambda handler function
        response = lambda_handler(event, None)
        
        # Parse the response body
        response_body = json.loads(response['body'])
        
        # Assert the response contains the correct bucket name and object key
        self.assertEqual(response_body['bucket_name'], 'my-test-bucket')
        self.assertEqual(response_body['object_key'], 'test-object.txt')
        self.assertEqual(response['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()