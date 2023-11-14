# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime
from boto3.dynamodb.conditions import Key, Attr

import json

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('ComMap')

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    response = table.scan(
    FilterExpression=Attr('ID').begins_with("")
    )
    items = response['Items']

    return items
