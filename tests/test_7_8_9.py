import pytest
from funciones import *
from curls import *

def test_case_7():
    datos_cp7_bd = caso_prueba7()
    datos_curl = curl_cp7()
    assert datos_cp7_bd["statusCode"] == datos_curl.status_code

def test_case_8():
    datos_cp8_bd = caso_prueba8()
    datos_curl = curl_cp8()
    assert datos_cp8_bd["code"] == datos_curl["code"]
    assert datos_cp8_bd["statusCode"] == datos_curl["statusCode"]

def test_case_9():
    datos_cp9_bd = caso_prueba9()
    datos_curl = curl_cp9()
    assert datos_cp9_bd["payload"] == datos_curl.json()
    assert datos_cp9_bd["statusCode"] == datos_curl.status_code
    