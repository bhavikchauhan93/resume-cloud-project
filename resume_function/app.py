import json
import boto3

def lambda_handler(event, context):
    dynamoDB = boto3.resource('dynamodb')
    table = dynamoDB.Table('cloud-resume-website-tbl')
    
    response = table.get_item(
        Key = {
            'ID': 'Visits'
        }
    )

    visit_count = response['Item']['Counter'] 
    visit_count = str(int(visit_count) + 1)
    print(visit_count)

    response = table.put_item(
        Item = {
            'ID':'Visits',
            'Counter': visit_count
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'Counter': visit_count
        })
    }