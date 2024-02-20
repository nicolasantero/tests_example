import pytest
from unittest.mock import patch
from functions.random_data import generate_random_user, generate_gender_specific_user

def test_generate_gender_specific_user_success():
    gender = 'male'
    number_of_users = 3
    users = generate_gender_specific_user(gender, number_of_users)
    assert all(user['gender'] == gender for user in users)


def test_generate_random_user_success():
    number_of_users = 3
    users = generate_random_user(number_of_users)
    assert len(users) == number_of_users
    assert all
