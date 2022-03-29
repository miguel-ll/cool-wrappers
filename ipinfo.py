import re
import json
import requests
#from urllib.request import urlopen
from geopy.geocoders import Nominatim
from faker import Faker
fake = Faker()


def ip_info(ipddr = fake.ipv4()):
    url = f'http://ipinfo.io/{ipddr}/json'   
    geoLoc = Nominatim(user_agent="GetLoc")
    resp = requests.get(url)
    data = resp.json()
    IP = data['ip']
    reg = data['region']
    city = data['city']
    country=data['country']
    timezone=data['timezone']
    latlon = data['loc']
    part1 = latlon.split(',', 1)[0]
    part2 = latlon.split(',', 1)[1]
    opm_link = f"https://www.openstreetmap.org/search?query={part1}%2C{part2}"
    try:
        hostname = data['hostname']
    except:
	    hostname = " "
    try:
        org = data['org']
    except:
        org = " "
    try:
        locname = geoLoc.reverse(str(latlon)).address
    except:
        locname = " "
    return IP, hostname, org, city, reg, country, timezone, latlon, locname, opm_link

def ip_infov2(ipddr = fake.ipv4()):
    url = f'http://ipinfo.io/{ipddr}/json'   
    geoLoc = Nominatim(user_agent="GetLoc")
    resp = requests.get(url)
    data = resp.json()
    IP = data['ip']
    reg = data['region']
    city = data['city']
    country=data['country']
    timezone=data['timezone']
    latlon = data['loc']
    part1 = latlon.split(',', 1)[0]
    part2 = latlon.split(',', 1)[1]
    opm_link = f"https://www.openstreetmap.org/search?query={part1}%2C{part2}"
    try:
        hostname = data['hostname']
    except:
        hostname = " "
    try:
        org = data['org']
    except:
        org = " "
    try:
        locname = geoLoc.reverse(str(latlon)).address
    except:
        locname = " "
    print('Your IP details:\n ')
    print(f'IP: {IP} \nHostname: {hostname} \nOrg: {org} \nCity: {city}\nRegion: {reg} \nCountry: {country} \nTimezone: {timezone} \nLat, Long: {latlon} \nFull Location: {locname} \nOPM LINK: {opm_link}')
