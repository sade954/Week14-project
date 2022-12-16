import boto3



new_dynamodb = boto3.resource('dynamodb')


table = new_dynamodb.create_table (
    AttributeDefinitions = [
        {
            'AttributeName': 'Network',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Title',
            'AttributeType': 'S'
        }
    ],
    TableName='TVShows',
    KeySchema=[
        {
             'AttributeName': 'Network',
             'KeyType': 'HASH'
        },
        {
             'AttributeName':'Title',
             'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
          
)

print(table)