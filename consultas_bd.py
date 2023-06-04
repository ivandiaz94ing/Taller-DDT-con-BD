import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

# Inicializa la aplicación Firebase con tus credenciales
cred = credentials.Certificate("bd-casos-de-prueba-firebase-adminsdk-rkwmw-0296e214af.json")
firebase_admin.initialize_app(cred, {
    "databaseURL":"https://bd-casos-de-prueba-default-rtdb.firebaseio.com/"
})

# Obtiene una referencia a la base de datos
ref_esperados = db.reference("/datos_esperados")
ref_entrada = db.reference("/datos_entrada")

# Obtiene los datos de Firebase
global datos_esperados
global datos_entrada

datos_esperados = ref_esperados.get()
datos_entrada = ref_entrada.get()

def caso_prueba1():
    
    cp1_str = datos_esperados["cp1"]
    cp1 = reemplazar_null_por_none(cp1_str)
    
    return cp1

def reemplazar_null_por_none(json_obj):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if value == "null":
                json_obj[key] = None
            else:
                reemplazar_null_por_none(value)
    elif isinstance(json_obj, list):
        for i in range(len(json_obj)):
            if json_obj[i] == "null":
                json_obj[i] = None
            else:
                reemplazar_null_por_none(json_obj[i])
    
    return json_obj

def caso_prueba2():

    cp2 = datos_esperados["cp2"]
    return cp2

def caso_prueba3():

    cp3 = datos_esperados["cp3"]
    return cp3

def caso_prueba4():

    cp4_str = datos_esperados["cp4"]
    cp4 = reemplazar_null_por_none(cp4_str)
    return cp4

def caso_prueba5():

    cp5 = datos_esperados["cp5"]
    return cp5

def caso_prueba6():

    cp6 = datos_esperados["cp6"]
    return cp6

def caso_prueba7():

    cp7 = datos_esperados["cp7"]
    return cp7

def caso_prueba8():

    cp8 = datos_esperados["cp8"]
    return cp8

def caso_prueba9():

    cp9 = datos_esperados["cp9"]
    return cp9

def caso_prueba10():
    cp10 = datos_esperados["cp10"]
    return cp10

def caso_prueba11():
    cp11 = datos_esperados["cp11"]
    return cp11

def caso_prueba12():
    cp12 = datos_esperados["cp12"]
    return cp12

def caso_prueba13():
    cp13 = datos_esperados["cp13"]
    return cp13

def caso_prueba14():
    cp14 = datos_esperados["cp14"]
    return cp14

def caso_prueba15():
    cp15 = datos_esperados["cp15"]
    return cp15




