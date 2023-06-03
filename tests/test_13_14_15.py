import pytest
from funciones import *
from curls import *

def test_case_13():
    datos_cp13_bd = caso_prueba13()
    datos_curl = curl_cp13()
    assert datos_cp13_bd["-NX-XqUwZvWDOs7uFram"] == datos_curl.json()
    assert datos_cp13_bd["statusCode"] == datos_curl.status_code

def test_case_14():
    datos_cp14_bd = caso_prueba14()
    datos_curl = curl_cp14()
    assert datos_cp14_bd["code"] == datos_curl["code"]
    assert datos_cp14_bd["statusCode"] == datos_curl["statusCode"]

def test_case_15():
    datos_cp15_bd = caso_prueba15()
    datos_curl = curl_cp15()
    assert datos_cp15_bd["code"] == datos_curl["code"]
    assert datos_cp15_bd["statusCode"] == datos_curl["statusCode"]