import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Trey, Welcome to the FT Gamification badge aug lambda')
    }
