import ctypes

def converter_menu():
    print("\n************** MENÚ DE CONVERSIÓN **************")
    print("Bienvenido al convertidor de temperaturas")
    print("[1] Convertir grados °C a °F")
    print("[2] Convertir grados °F a °C")
    print("[0] Salir del programa \n")
    
def convert_c_to_f(p_temp_celsius:int) -> int:
    temp_fahr = round((9/5)*p_temp_celsius+32)
    return temp_fahr

def convert_f_to_c(p_temp_fahr:int) -> int:
    temp_celsius = round((p_temp_fahr - 32) * (5/9))
    return temp_celsius

