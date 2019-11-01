# You don't have to use these classes, but we recommend them as a good place to start!

class MongoHandler():
    pass


class WeatherGetter():
    def __init__(self, date = None):
    self.key = “DATAKEY” #add key here 
    self.date = date + “T12:00:00”  #default time is set to 12pm
      self.lat = 52.52 # Latitude for Berlin
      self.long = 13.4050 #Longitude for Berlin
      self.key = “DATAKEY” #add key here
      self.link = f”https://api.darksky.net/forecast/{self.key}/{self.lat},{self.long},{self.date}?exclude=currently,hourly,flags”
      self.weather = self.getweathersummary()
  def getweathersummary(self):
      r = requests.get(self.link)
      response = r.json() #parse result as json file.
      try:
          response[‘daily’][‘data’][0][‘icon’]
      except:
          return response[‘daily’][‘data’][0][‘summary’]  #if there is no icon then get summary
      else:
          return response[‘daily’][‘data’][0][‘icon’]