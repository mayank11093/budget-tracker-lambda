import json
import boto3
import uuid

def lambda_handler(event, context):
    print(event)
    expenseId = str(uuid.uuid4())
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('expenses')
    putResponse = table.put_item(
       Item={
            'user': event.get('user'),
            'expenseId': expenseId,
            'dateOfExpense': event.get('dateOfExpense'),
            'expenseFor': event.get('expenseFor'),
            'amount': event.get('amount'),
            'category': event.get('category'),
            'notForMe': event.get('notForMe'),
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