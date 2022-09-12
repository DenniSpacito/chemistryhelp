import requests
import json

raw_data = requests.get("https://periodic-table-elements-info.herokuapp.com/elements") # get periodic table data

datatable = json.loads(raw_data.text) # load data into a python list

user_element = input("What element do you want information on? (1, He, Boron)..").lower()

def parse_user_response_type(response):
    if len(response) >= 4:
        return 'name'
    else:
        for i in range(9):
            if int(response[0]) == i:
                return 'atomicnumber'
        return 'symbol'

response_type = parse_user_response_type(user_element)

def verify_response_validity(response, response_type):
    if response_type == 'symbol':
        for elem in datatable:
            if user_element == elem['symbol'].lower():
                print(elem)
    elif response_type == 'atomicnumber':
        for elem in datatable:
            if int(user_element) == elem['atomicNumber']:
                print(elem)
    elif response_type == 'name':
        for elem in datatable:
            if user_element == elem['name'].lower():
                print(elem)
    
verify_response_validity(user_element, response_type)
