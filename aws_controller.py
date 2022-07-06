import boto3
from boto3.dynamodb.conditions import Key


dynamo_client = boto3.client('dynamodb')


def get_items():
    return dynamo_client.scan(
        TableName='CSC3004_Table'
    )


def get_latest_update():
    response = dynamo_client.scan(
        TableName='CSC3004_Table',
    )
    return response['Items'][-1]['number_of_People']['N']
