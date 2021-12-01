import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    response = {}
    username = event['username']
    password = event['password']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    scan_kwargs = {
        'FilterExpression': Key('username').eq(username) & Key('password').eq(password)
    }

    scanResponse = table.scan(**scan_kwargs)
    print(scanResponse['Items'])
    if len(scanResponse['Items']) == 1:
        print('Success')
        response = createResponse(scanResponse['Items'],200)
    else:
        print('Failed')
        response = createResponse([],401)
    
    return response

def createResponse(itemList, status):
    res = {}
    if status == 200:
        res['userName'] = itemList[0]['username']
        res['fullName'] = itemList[0]['name']
        res['userId'] = str(itemList[0]['userId'])
    else:
         res['message'] = 'Invalid credentials. Please try with correct one.'
    return {
        'statusCode': status,
        'body': json.dumps(res)
    }