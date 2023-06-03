import requests
import pytest
from connection import get_collection

collection = get_collection()
headers = collection.find_one()["headers"]
invalid = collection.find_one()["invalid_token"]
unexist = collection.find_one()["unexist_token"]
user_id = "d65c27dc-b02c-4fd8-9d8e-09f3c90f12d9"


#Test metodo GET v0.1/user
def test_get_user():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=headers)
    data = response.json()

    expected = collection.find_one()["test_1"]["expected"]
    assert data["name"] == expected

def test_get_user_invalid():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=invalid)
    data = response.json()

    expected = collection.find_one()["test_2"]["expected"]
    assert data["statusCode"] == expected

def test_get_user_unexist():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=unexist)
    data = response.json()

    expected = collection.find_one()["test_3"]["expected"]
    assert data["statusCode"] == expected



#Test metodo POST v0.1/users/{user_id}/devices/register
def test_post_devices_register():
    url = f"https://api.appcenter.ms/v0.1/users/{user_id}/devices/register"

    payload = collection.find_one()["test_4"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    
    expected = collection.find_one()["test_4"]["expected"]
    assert data["model"] == expected

def test_post_devices_invalid():
    url = f"https://api.appcenter.ms/v0.1/users/{user_id}/devices/register"

    payload = collection.find_one()["test_5"]["payload"]
    response = requests.post(url, headers=invalid, json=payload)
    data = response.json()

    
    expected = collection.find_one()["test_5"]["expected"]
    assert data["statusCode"] == expected

def test_post_devices_unexist():
    url = f"https://api.appcenter.ms/v0.1/users/{user_id}/devices/register"

    payload = collection.find_one()["test_6"]["payload"]
    response = requests.post(url, headers=unexist, json=payload)
    data = response.json()

    
    expected = collection.find_one()["test_6"]["expected"]
    assert data["statusCode"] == expected



#Test metodo GET v0.1/user/devices
def test_get_device():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url, headers=headers)
    data = response.json()

    expected = collection.find_one()["test_7"]["expected"]
    assert data[0]["udid"] == expected

def test_get_device_invalid():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url, headers=invalid)
    data = response.json()

    expected = collection.find_one()["test_8"]["expected"]
    assert data["statusCode"] == expected


def test_get_device_unexist():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url, headers=unexist)
    data = response.json()

    expected = collection.find_one()["test_9"]["expected"]
    assert data["statusCode"] == expected



#Test metodo GET v0.1/users/devices/{device_udid}
def test_get_device_udid():
    url = f"https://api.appcenter.ms/v0.1/user/devices/0001"

    response = requests.get(url, headers=headers)
    data = response.json()

    expected = collection.find_one()["test_10"]["expected"]
    assert data["model"] == expected

def test_get_device_udid_invalid():
    url = f"https://api.appcenter.ms/v0.1/user/devices/0001"

    response = requests.get(url, headers=invalid)
    data = response.json()

    expected = collection.find_one()["test_11"]["expected"]
    assert data["statusCode"] == expected

def test_get_device_udid_unexist():
    url = f"https://api.appcenter.ms/v0.1/user/devices/0001"

    response = requests.get(url, headers=unexist)
    data = response.json()

    expected = collection.find_one()["test_12"]["expected"]
    assert data["statusCode"] == expected



#Test metodo POST v0.1/orgs
def test_post_orgs():
    url = f"https://api.appcenter.ms/v0.1/orgs"

    payload = collection.find_one()["test_13"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    expected = collection.find_one()["test_13"]["expected"]
    assert data["name"] == expected

def test_post_orgs_invalid():
    url = f"https://api.appcenter.ms/v0.1/orgs"

    payload = collection.find_one()["test_14"]["payload"]
    response = requests.post(url, headers=invalid, json=payload)
    data = response.json()

    expected = collection.find_one()["test_14"]["expected"]
    assert data["statusCode"] == expected

def test_post_orgs_unexist():
    url = f"https://api.appcenter.ms/v0.1/orgs"

    payload = collection.find_one()["test_15"]["payload"]
    response = requests.post(url, headers=unexist, json=payload)
    data = response.json()

    expected = collection.find_one()["test_15"]["expected"]
    assert data["statusCode"] == expected
