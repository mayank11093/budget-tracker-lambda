import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    username = event.get('params').get('path').get('user')
    id_ = event.get('params').get('path').get('id')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('income')
    response = table.delete_item(
        Key={
            'user': username,
            'id': id_,
        }
    )
    if response.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        print('Success')
        return True
    else:
        print('Failed')
        return False