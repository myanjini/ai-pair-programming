import json

def lambda_handler(event, context):
    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Print bucket name and object key
    print(f"Bucket Name: {bucket_name}")
    print(f"Object Key: {object_key}")
    
    # Return bucket name and object key as JSON
    response = {
        'bucket_name': bucket_name,
        'object_key': object_key
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }