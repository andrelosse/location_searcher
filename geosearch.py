import json
from geopy.geocoders import Nominatim


def searchloc(search):

    geolocator = Nominatim(user_agent="wazeyes")
    location = geolocator.geocode(search)

    infos = [location.address, location.latitude, location.longitude]
    return infos


def writesearch(search):

    try:
        with open("address.json", "w") as endjson:
            json.dump(search, endjson)
        print("Endereço gravado!")

    except Exception:
        print("Cannot write file...")


def readsearch():

    try:
        with open("address.json", "r") as newend:
            search_loaded = json.load(newend)
            return search_loaded

    except FileNotFoundError:
        print("File does not exit...")


def writecoords(location):

    try:

        with open("coordinates.json", "w") as latlon:
            json.dump(location, latlon)

    except Exception:

        print("Cannot write coordinates on file...")
