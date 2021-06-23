import requests
import random

def find_city(pincode):
    api_address = "https://api.postalpincode.in/pincode/"

    #pincode = input('Pincode: ')
    url = api_address + pincode

    data_json = requests.get(url).json()
    try:
        if(data_json[0]['PostOffice'][0]['State'] == "Delhi"):
            final_city = data_json[0]['PostOffice'][0]['State']

        else:
            final_city = data_json[0]['PostOffice'][0]['District']
    except:
        final_city = "Not available at the moment"

    return final_city

def find_resource(city,resource):

    url = "http://ec2-3-23-130-174.us-east-2.compute.amazonaws.com:8000/resource?city="+city+"&category="+resource

    data_json = requests.get(url).json()

    cov_resource = []
    var = 0


    for data in data_json["data"]:
        var +=1
        cov_resource.append(data)

    if(cov_resource):
        return cov_resource[random.randrange(var)]

    else:
        return "None"

    
        
    








