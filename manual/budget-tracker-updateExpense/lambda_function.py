import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    username = event.get('params').get('path').get('user')
    expenseId = event.get('params').get('path').get('expenseId')
    dateOfExpense = event.get('body-json').get('dateOfExpense')
    expenseFor = event.get('body-json').get('expenseFor')
    amount = event.get('body-json').get('amount')
    category = event.get('body-json').get('category')
    notForMe = event.get('body-json').get('notForMe')
    description = event.get('body-json').get('description')
    eID = event.get('body-json').get('expenseId')
    if eID != expenseId:
        print('different ')
        return False
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('expenses')
    putResponse = table.update_item(
      Key={
            'user': username,
            'expenseId': expenseId
        },
        UpdateExpression="set dateOfExpense=:dateOfExpense, expenseFor=:expenseFor, amount=:amount, category=:category, notForMe=:notForMe, description=:description",
        ExpressionAttributeValues={
            ':dateOfExpense': dateOfExpense,
            ':expenseFor': expenseFor,
            ':amount': amount,
            ':category': category,
            ':notForMe': notForMe,
            ':description': description    
        },
        ReturnValues="UPDATED_NEW"
    )
    print(putResponse)
    if putResponse.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        print('Success')
        return True
    else:
        print('Failed')
        return False