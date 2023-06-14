import ctypes
from retrying import retry

## Alert button information
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

@retry
def get_player_choice() -> int:

    try:
        user_choice = int(input("\nSeleccione la jugada:\n1. Piedra\n2. Papel\n3. Tijera\n"))

    except:
        ctypes.windll.user32.MessageBoxW(0, "Trate nuevamente.\nNo se permiten: decimales, negativos y letras!\nSolamente se permite seleccionar entre 1 y 3", "Error",  ICON_EXCLAIM)
    
    return user_choice

def get_choice_name(p_user_choice:int) -> str:

    if p_user_choice == 1: 
        choice_name = "Piedra"
    elif p_user_choice == 2:
        choice_name = "Papel"
    else:
        choice_name = "Tijera"
    
    return choice_name

def get_player_1_data() -> dict:
    player_data = {}
    username = ""

    username = input("Jugador 1 ingrese su nombre de usuario:\n")
    user_choice = get_player_choice()
    choice_name = get_choice_name(user_choice)

    player_data["username"] = username
    player_data["choice"] = user_choice
    player_data["choice_name"] = choice_name

    return player_data

@retry
def get_player_2_data() -> dict:
    player_data = {}
    username = ""
    

    username = input("Jugador 2 ingrese su nombre de usuario:\n")
    user_choice = get_player_choice()
    choice_name = get_choice_name(user_choice)

    player_data["username"] = username
    player_data["choice"] = user_choice
    player_data["choice_name"] = choice_name

    return player_data

def verify_winner(p_p1:dict, p_p2:dict) -> str:
    msg = ""

    if p_p1["choice_name"] == p_p2["choice_name"]:
        msg = (f"Ambos jugadores seleccionaron {p_p1['choice_name']}. Esto es un empate!")

    elif p_p1["choice_name"] == "Papel":
        if p_p2["choice_name"] == "Piedra":
            msg = (f"{p_p1['choice_name']} vence a {p_p2['choice_name']} - {p_p1['username']} ha ganado el juego felicidades!!")
        else:
            msg = (f"{p_p2['choice_name']} vence a {p_p1['choice_name']} - {p_p2['username']} ha ganado el juego felicidades!!")

    elif p_p1["choice_name"] == "Piedra":
        if p_p2["choice_name"] == "Tijera":
            msg = (f"{p_p1['choice_name']} vence a {p_p2['choice_name']} - {p_p1['username']} ha ganado el juego felicidades!!")
        else:
            msg = (f"{p_p2['choice_name']} vence a {p_p1['choice_name']} - {p_p2['username']} ha ganado el juego felicidades!!")

    elif p_p1["choice_name"] == "Tijera":
        if p_p2["choice_name"] == "Papel":
            msg = (f"{p_p1['choice_name']} vence a {p_p2['choice_name']} - {p_p1['username']} ha ganado el juego felicidades!!")
        else:
            msg = (f"{p_p2['choice_name']} vence a {p_p1['choice_name']} - {p_p2['username']} ha ganado el juego felicidades!!")
        
    return msg

# ######## TO DO ######## # 

# @retry
# def validate_choice(p_user_choice) -> int:
#     try:
#         if p_user_choice in range(1,4):
#             return p_user_choice
#     except:
#         ctypes.windll.user32.MessageBoxW(0, "\nSolamente se permite seleccionar entre 1 y 3\n", "Error",  ICON_EXCLAIM)