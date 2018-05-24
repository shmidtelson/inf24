import urllib.request, json


# Grabbing and parsing the JSON data
def GoogPlac(lat, lng, radius, types, key):
    # making the url
    AUTH_KEY = key
    LOCATION = str(lat) + "," + str(lng)
    RADIUS = radius
    TYPES = types
    MyUrl = ('https://maps.googleapis.com/maps/api/place/radarsearch/json'
             '?location=%s'
             '&radius=%s'
             '&types=%s'
             '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
    # grabbing the JSON result
    with urllib.request.urlopen(MyUrl) as url:
        jsonRaw = url.read()
    jsonData = json.loads(jsonRaw)

    return jsonData


# This is a helper to grab the Json data that I want in a list
def IterJson(place):
    x = [place['name'], place['reference'], place['geometry']['location']['lat'],
         place['geometry']['location']['lng'], place['vicinity']]
    return x


data = GoogPlac(53.9, 27.56667, 20000, 'pharmacy', 'AIzaSyBYPb81GpPYXWv708c1rfe_krcGtCojdAM')

print(data)
# for key,value in data["results"]:
#     print(key,value)
