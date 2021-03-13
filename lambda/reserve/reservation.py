class Reservation:
  def __init__(self, params):
    self.name = params['name']
    self.email = params['email']
    self.telephone = params['telephone']
    self.date = params['date']
    self.time = params['time']
    self.party = params['party']
    self.message = params['message']
    

