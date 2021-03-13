import json, boto3, uuid
from reservation import Reservation

from pprint import pprint

def lambda_handler(event, context):
    
    params = event['queryStringParameters']
    
    if params_missing_mandatory_fields(params):
        return error_response(500, 'missing mandatory fields')
        
    if params_contain_bad_vals(params):
        return error_response(500, 'bad vals')
    
    reservation = Reservation(params)
    save_to_dynamo(reservation)
    
    return {
        'statusCode': 200,
        'body': 'success'
    }

def params_missing_mandatory_fields(params):
    return 'name' not in params or 'email' not in params or 'party' not in params or 'date' not in params or 'time' not in params

def params_contain_bad_vals(params):
    return is_not_valid_party(params['party']) or is_not_valid_str(params['name']) or is_not_valid_str(params['email']) or is_not_valid_str(params['date']) or is_not_valid_str(params['time'])

def is_not_valid_party(party):
    return int(party) < 1
    
def is_not_valid_str(s):
    return len(s.strip()) == 0

def error_response(statusCode, msg):
    return {
        'statusCode': statusCode,
        'body': json.dumps(msg)
    }
    
def save_to_dynamo(reservation):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Reservations')
    table.put_item(
       Item = {
            'Id': str(uuid.uuid4()),
            'Name': reservation.name,
            'Email': reservation.email,
            'Telephone': reservation.telephone,
            'Date': reservation.date,
            'Time': reservation.time,
            'Party': reservation.party,
            'Message': reservation.message
        }
    )

