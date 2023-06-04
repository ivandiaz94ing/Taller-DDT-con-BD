import pytest
from consultas_bd import *
from curls import *

def test_case_10():
    datos_cp10_bd = caso_prueba10()
    datos_curl = curl_cp10()
    assert datos_cp10_bd["statusCode"] == datos_curl.status_code

def test_case_11():
    datos_cp11_bd = caso_prueba11()
    datos_curl = curl_cp11()
    assert datos_cp11_bd["payload"] == datos_curl.json()
    assert datos_cp11_bd["statusCode"] == datos_curl.status_code

def test_case_12():
    datos_cp12_bd = caso_prueba12()
    datos_curl = curl_cp12()
    assert datos_cp12_bd["code"] == datos_curl["code"]
    assert datos_cp12_bd["statusCode"] == datos_curl["statusCode"]