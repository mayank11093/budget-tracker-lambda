import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    username = event.get('params').get('path').get('user')
    id_ = event.get('params').get('path').get('id')
    dateOfIncome = event.get('body-json').get('dateOfIncome')
    title = event.get('body-json').get('title')
    amount = event.get('body-json').get('amount')
    incomeSource = event.get('body-json').get('incomeSource')
    description = event.get('body-json').get('description')
    iID = event.get('body-json').get('id')
    if iID != id_:
        print('different ')
        return False
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('income')
    putResponse = table.update_item(
      Key={
            'user': username,
            'id': id_
        },
        UpdateExpression="set dateOfIncome=:dateOfIncome, title=:title, amount=:amount, incomeSource=:incomeSource, description=:description",
        ExpressionAttributeValues={
            ':dateOfIncome': dateOfIncome,
            ':title': title,
            ':amount': amount,
            ':incomeSource': incomeSource,
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