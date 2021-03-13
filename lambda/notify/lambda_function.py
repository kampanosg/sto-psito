import json, os, data_factory, requests
from mailjet_rest import Client
from reservation import Reservation

api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']

sms_admin_phone = os.environ['SMS_ADMIN_PHONE']
sms_token = os.environ['SMS_JWT_TOKEN']

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

def lambda_handler(event, context):
    records = event['Records']
    records = list(filter(lambda record: record['eventName'] == 'INSERT', records))
    records = list(map(lambda record: Reservation(record), records))

    for record in records:
        send_email_to_customer(record)
        send_sms_to_admin(record)
        
    return {
        'statusCode': 200,
        'body': 'success'
    }
    
def send_email_to_customer(reservation):
    mailjet.send.create(data=data_factory.get_data_for_customer(reservation))

def send_sms_to_admin(reservation):
    url = "https://api.thesmsworks.co.uk/v1/message/send"
    
    payload = "{\n\"sender\": \"StoPsito\",\n\"destination\":\"" + sms_admin_phone +"\",\n\"content\":\"" + build_sms_content(reservation) +"\",\n\"deliveryreporturl\": \"\",\n\"schedule\": \"\",\n\"tag\": \"RSRV1\"}"
    headers = {
      'Authorization': sms_token,
      'Content-Type': 'application/json'
    }
    
    requests.request("POST", url, headers=headers, data=payload)

def build_sms_content(reservation):
    return 'Reservation\\nName: {0}\\nPhone:{1}\\nParty: {2}\\nDate: {3}\\nTime: {4}\\nMsg: {5}'.format(reservation.name, reservation.telephone, reservation.party, reservation.date, reservation.time, reservation.message)
