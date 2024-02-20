import requests

def generate_random_user(number_of_users):
    url = f'https://randomuser.me/api/?results={number_of_users}'
    response = requests.get(url)
    return response.json()['results']

def generate_gender_specific_user(gender, number_of_users):
    url = f'https://randomuser.me/api/?results={number_of_users}&gender={gender}'
    response = requests.get(url)
    return response.json()['results']
