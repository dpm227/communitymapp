# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('ComMap')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# Initialize the AWS Location client
location_client = boto3.client('location')

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    name = str(event['name'])
    address = str(event['long'])
    comment = str(event['comment'])
    
    attributes = name + "|" + address + "|" + "|" + comment
    
    # ADD THIS TO EXISTING PYTHON FUNCTION

    # Specify the address you want to geocode
    #address = "1600 Amphitheatre Parkway, Mountain View, CA"
    
    # Call the Geocode API
    addressResponse = location_client.search_place_index_for_text(
        IndexName='TestPlaceIndex',
        Text=address,
        MaxResults=1,
        BiasPosition = [-75.480858, 40.632950]
    )
    
    # Extract the coordinates from the response
    coordinates = addressResponse['Results'][0]['Place']['Geometry']['Point']
    
    mycoordinates = (str(coordinates[1]), (str(coordinates[0])))
    
    # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': name,
            'address': address,
            'lat': str(coordinates[1]),
            'long': str(coordinates[0]),
            'comment': comment,
            'LatestGreetingTime':now
            })
    
    return
    {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + coordinates)
    }

