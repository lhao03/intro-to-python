import requests

# function that checks to see if API is OK
# if 200 is returned, this means the API can be used 
def check_request(endpoint):
    response = requests.get(endpoint)
    return response.status_code == 200

# function that returns json
def get_request(endpoint):
    response = requests.get(endpoint)
    json = response.json()
    return list(json)
