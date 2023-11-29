import json
import urllib3

def lambda_handler(event, context):
    url="https://pokeapi.co/api/v2/pokemon"
    http = urllib3.PoolManager()
    response = http.request('GET',url)
    res_data = response.data
    decoded_result = res_data.decode('utf-8')

    return {
        'statusCode': 200,
        'body': json.loads(decoded_result)
    }