import boto3

dynamo_client = boto3.client('dynamodb', region_name='us-west-2')


def get_items():
    return dynamo_client.scan(
        TableName='CSC3004'
    )

def get_latest_update():
    response = dynamo_client.scan(
        TableName='CSC3004_Table'
    )
    return response['Items'][-1]['number_of_People']['N']