import googlemaps
gmaps = googlemaps.Client(key='AIzaSyC0AuanxSq5DMmcnojnInlFRzqz0KF5HZI')
print(gmaps.client_id)
rad = 50
path= "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + "50" + "," + "50" + "&radius=" + "50" + "&type=restaurant&keyword=cruise&key=AIzaSyC0AuanxSq5DMmcnojnInlFRzqz0KF5HZI"
print(path)