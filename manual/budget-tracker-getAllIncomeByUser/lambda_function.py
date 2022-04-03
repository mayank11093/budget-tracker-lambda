import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # TODO implement
    print(event)
    username = event.get('params').get('path').get('user')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('income')
    queryResponse = table.query(
        KeyConditionExpression=Key('user').eq(username)
    )
    response = createResponse(queryResponse['Items'],200)
    return response
        

def createResponse(itemList, status):
    res = {}
    if status == 200:
        res = itemList
    else:
        res['message'] = 'Invalid credentials. Please try with correct one.'
    return  res
    