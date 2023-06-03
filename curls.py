import requests
import json
from funciones import *

def curl_cp1():
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
    "accept": "application/json",
    "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e" 
    }

    response = requests.get(url, headers=headers)

    return response

def curl_cp2():
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
        "accept": "aplication/json",
        "X-API-Token" : "tokenIncorrecto"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def curl_cp3():
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
        "accept": "aplication/json"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def curl_cp4():
    cp4 = datos_entrada["cp4"]
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
        "accept" : "application/json",
        "X-API-Token" : "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type" : "application/json"
    }

    data = {
        "display_name": cp4["display_name"]
    }

    response = requests.patch(url, headers=headers, data=json.dumps(data))

    return response

def curl_cp5():
    cp5 = datos_entrada["cp5"]
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
        "accept" : "application/json",
        "X-API-Token" : "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type" : "application/json"
    }

    data = {
        "display_name": cp5["display_name"]
    }

    response = requests.patch(url, headers=headers, data=json.dumps(data))

    return response

def curl_cp6():
    url = "https://api.appcenter.ms/v0.1/user"
    headers = {
        "accept" : "application/json",
        "X-API-Token" : "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type" : "application/json"
    }

    data = {
        
    }

    response = requests.patch(url, headers=headers, data=data)

    return response

def curl_cp7():
    cp7 = datos_entrada["cp7"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/invitations"
    url_nueva = url.replace("{dato}", cp7["org_name"])
    headers = {
        "accept": "application/json",
        "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type": "application/json"
    }
    data = {
        "user_email": cp7["user_email"]
    }

    response = requests.delete(url_nueva, headers=headers, data=json.dumps(data))

    return response

def curl_cp8():
    cp8 = datos_entrada["cp8"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/invitations"
    url_nueva = url.replace("{dato}", cp8["org_name"])
    headers = {
        "accept": "application/json",
        "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type": "application/json"
    }
    data = {
        "user_email": cp8["user_email"]
    }

    response = requests.delete(url_nueva, headers=headers, data=json.dumps(data))

    return response.json()

def curl_cp9():
    cp9 = datos_entrada["cp9"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/invitations"
    url_nueva = url.replace("{dato}", cp9["org_name"])
    headers = {
        "accept": "application/json",
        "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type": "application/json"
    }
    data = {
        "user_email": cp9["user_email"]
    }

    response = requests.delete(url_nueva, headers=headers, data=json.dumps(data))

    return response

def curl_cp10():
    cp10 = datos_entrada["cp10"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/invitations"
    url_nueva = url.replace("{dato}", cp10["org_name"])
    headers = {
        "accept": "application/json",
        "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type": "application/json"
    }
    data = {
        "user_email": cp10["user_email"],
        "role": cp10["role"]
    }

    response = requests.post(url_nueva, headers=headers, data=json.dumps(data))

    return response

def curl_cp11():
    cp11 = datos_entrada["cp11"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/invitations"
    url_nueva = url.replace("{dato}", cp11["org_name"])
    headers = {
        "accept": "application/json",
        "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type": "application/json"
    }
    data = {
        "user_email": cp11["user_email"],
        "role": cp11["role"]
    }

    response = requests.post(url_nueva, headers=headers, data=json.dumps(data))

    return response

def curl_cp12():
    cp12 = datos_entrada["cp12"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/invitations"
    url_nueva = url.replace("{dato}", cp12["org_name"])
    headers = {
        "accept": "application/json",
        "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e",
        "Content-Type": "application/json"
    }
    data = {
        "user_email": cp12["user_email"],
        "role": cp12["role"]
    }

    response = requests.post(url_nueva, headers=headers, data=json.dumps(data))

    return response.json()

def curl_cp13():
    cp13 = datos_entrada["cp13"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/teams"
    url_nueva = url.replace("{dato}", cp13["org_name"])
    headers = {
    "accept": "application/json",
    "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e" 
    }

    response = requests.get(url_nueva, headers=headers)

    return response

def curl_cp14():
    cp14 = datos_entrada["cp14"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/teams"
    url_nueva = url.replace("{dato}", cp14["org_name"])
    headers = {
    "accept": "application/json",
    "X-API-Token": "79997fa7c82449961399867174d876d2872dfb5e" 
    }

    response = requests.get(url_nueva, headers=headers)

    return response.json()

def curl_cp15():
    cp15 = datos_entrada["cp15"]
    url = "https://api.appcenter.ms/v0.1/orgs/{dato}/teams"
    url_nueva = url.replace("{dato}", cp15["org_name"])
    headers = {
    "accept": "application/json",
    "X-API-Token": "TokenInvalido" 
    }

    response = requests.get(url_nueva, headers=headers)

    return response.json()

