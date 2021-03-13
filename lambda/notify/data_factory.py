def get_data_for_customer(reservation):
    return {'Messages': [{
        'From': {'Email': 'stopsito.restaurant@gmail.com',
                 'Name': 'Sto Psito Restaurant'},
        'To': [{'Email': reservation.email, 'Name': reservation.name}],
        'Bcc': [{'Email': 'stopsito.restaurant@gmail.com',
                'Name': 'Sto Psito Restaurant'}],
        'TemplateID': 2620805,
        'TemplateLanguage': True,
        'Subject': 'Your reservation has been confirmed!',
        'Variables': {
            'name': reservation.name,
            'date': reservation.date,
            'time': reservation.time,
            'party': reservation.party,
            'email': reservation.email,
            'message': reservation.message,
            },
        }]}

