import pytest
from funciones import *
from curls import *

def test_case_1():
    datos_cp1_bd = caso_prueba1()
    datos_curl = curl_cp1()
    assert datos_cp1_bd["payload"] == datos_curl.json()
    assert datos_cp1_bd["status_code"] == datos_curl.status_code

def test_case_2():
    datos_cp2_bd = caso_prueba2()
    datos_curl = curl_cp2()
    assert datos_cp2_bd["statusCode"] == datos_curl["statusCode"]
    assert datos_cp2_bd["code"] == datos_curl["code"]

def test_case_3():
    datos_cp3_bd = caso_prueba3()
    datos_curl = curl_cp3()
    assert datos_cp3_bd["statusCode"] == datos_curl["statusCode"]
    assert datos_cp3_bd["code"] == datos_curl["code"]