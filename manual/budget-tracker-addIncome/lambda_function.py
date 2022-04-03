import json
import boto3
import uuid

def lambda_handler(event, context):
    print(event)
    expenseId = str(uuid.uuid4())
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('income')
    putResponse = table.put_item(
       Item={
            'user': event.get('user'),
            'id': expenseId,
            'dateOfIncome': event.get('dateOfIncome'),
            'title': event.get('title'),
            'amount': event.get('amount'),
            'incomeSource': event.get('incomeSource'),
            'description': event.get('description')
        }
    )
    response = {}
    if putResponse.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        print('Success')
        return True
    else:
        print('Failed')
        return False