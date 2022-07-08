import boto3

dynamo_client = boto3.client('dynamodb', region_name='us-west-2')


def get_items():
    return dynamo_client.scan(
        TableName='CSC3004_Table'
    )


def get_latest_update_1():
    response = dynamo_client.scan(
        TableName='CSC3004_Table'
    )
    return response['Items'][-1]['number_of_People']['N']


def get_latest_update_2():
    response = dynamo_client.scan(
        TableName='CSC3004_Table1'
    )
    return response['Items'][-1]['number_of_People']['N']