"""
source:
    http://stackoverflow.com/questions/18807114/http-error-403-with-api-id-in-accessing-google-maps
"""
import urllib, json, csv


def geocode(addr):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" %   (urllib.quote(addr.replace(' ', '+')))
    data = urllib.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")
    #A little ugly I concede, but I am open to all advices :) '''
    return info


#Open the List file of adresses to look for corresponding lat and lng.
f = open('list', 'rb')
addresses = f.readlines()
f.close()

#Loop to feed the func with adresses and output the lat & lng.
for a in addresses:
    r = geocode(a)
    print "%s %s" % (r['lat'], r['lng'])