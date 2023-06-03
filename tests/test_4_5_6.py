import pytest
from funciones import *
from curls import *

def test_case_4():
    datos_cp4_bd = caso_prueba4()
    datos_curl = curl_cp4()
    assert datos_cp4_bd["payload"] == datos_curl.json()
    assert datos_cp4_bd["statusCode"] == datos_curl.status_code

def test_case_5():
    datos_cp5_bd = caso_prueba5()
    datos_curl = curl_cp5()
    assert datos_cp5_bd["payload"] == datos_curl.json()
    assert datos_cp5_bd["statusCode"] == datos_curl.status_code

def test_case_6():
    datos_cp6_bd = caso_prueba6()
    datos_curl = curl_cp6()
    assert datos_cp6_bd["payload"] == datos_curl.json()
    assert datos_cp6_bd["statusCode"] == datos_curl.status_code