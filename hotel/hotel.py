class Hotel:
  def __init__(self, maxNumberGuests, numberParking):
    self.maxNumberGuests = maxNumberGuests
    self.numberParking = numberParking
    self.guests = 0

  def checkin(self, numberGuests):
    self.guests += numberGuests

  def checkout(self, numberGuests):
    self.guests -= numberGuests

  def totalGuests (self):
    return self.guests

# Hotel instance
hotelJoans = Hotel(maxNumberGuests=50, numberParking=25)

print(f'Maximum number of guests: {hotelJoans.maxNumberGuests}')
print(f'Number of parkings: {hotelJoans.numberParking}')

print(f'*'*30)
print(f'Ckeckin March 24th')
hotelJoans.checkin(7)
print(f'Number of guests: {hotelJoans.guests}')

print(f'*'*30)
print(f'Ckeckout March 25th')
hotelJoans.checkout(3)
print(f'Number of guests: {hotelJoans.guests}')

