import json

# This code goes into Lambda

def lambda_handler(event, contact):
    comment = str(event['base'])