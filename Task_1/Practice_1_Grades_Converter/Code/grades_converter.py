from gc_functions import *
import ctypes

# buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10

converter_menu()
option_menu = int(input("Seleccione una opción: \n"))

while option_menu != 0:
    if option_menu == 1:
        try:
            temp_celsius = int(input("Ingrese la temperatura en °C: \n"))
            temp_fahr = convert_c_to_f(temp_celsius)
            msg = f"\nResultado: {temp_celsius}°C equivalen a {temp_fahr}°F"
            print(msg)
            pass
        except:
            ctypes.windll.user32.MessageBoxW(0, "No se permiten temperaturas con decimales.\nTrate nuevamente.", "Error",  ICON_STOP)
        
    elif option_menu == 2:
        try:
            temp_fahr = int(input("Ingrese la temperatura en °F: \n"))
        except:
            ctypes.windll.user32.MessageBoxW(0, "No se permiten temperaturas con decimales.\nTrate nuevamente.", "Error",  ICON_STOP)
        else:
            temp_celsius = convert_f_to_c(temp_fahr)
            msg = f"\nResultado: {temp_fahr}°F equivalen a {temp_celsius}°C"
            print(msg)
            pass

    else:
        msg = "Opción incorrecta."
        print(msg)

    converter_menu()
    option_menu = int(input("Seleccione una opción: \n"))

print("\nGracias por usar el sistema de conversión.\n")