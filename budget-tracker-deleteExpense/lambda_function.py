import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    username = event.get('params').get('path').get('user')
    expenseId = event.get('params').get('path').get('expenseId')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('expenses')
    response = table.delete_item(
        Key={
            'user': username,
            'expenseId': expenseId,
        }
    )
    if response.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        print('Success')
        return True
    else:
        print('Failed')
        return False