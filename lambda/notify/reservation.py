class Reservation:

    def __init__(self, params):
        entry = params['dynamodb']['NewImage']
        self.name = entry['Name']['S']
        self.email = entry['Email']['S']
        self.party = entry['Party']['S']
        self.date = entry['Date']['S']
        self.time = entry['Time']['S']
        self.message = entry['Message']['S']
        self.telephone = entry['Telephone']['S']
