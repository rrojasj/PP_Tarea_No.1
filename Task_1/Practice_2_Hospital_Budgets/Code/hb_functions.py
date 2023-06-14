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

## Functions
@retry
def get_nbs_data() -> int:
    try:
        p_nbs = int(input("\nIngrese la cantidad de partos naturales:\n"))
    except:
        ctypes.windll.user32.MessageBoxW(0, "No se permite la cantidad con decimales.\nTrate nuevamente.", "Error",  ICON_STOP)

    return p_nbs

@retry
def get_cbs_data() -> int:
    try:
        p_cbs = int(input("\nIngrese la cantidad de partos por cesárea:\n"))
    except:
        ctypes.windll.user32.MessageBoxW(0, "No se permite la cantidad con decimales.\nTrate nuevamente.", "Error",  ICON_STOP)

    return p_cbs

def validate_births(p_nbs:int, p_cbs:int) -> dict:
    if p_cbs >= (p_nbs*2):
        bud_areas = {
            "emerg_budget": 20,
            "surg_budget": 40,
            "matern_budget": 40
            }
    else:
        bud_areas = {
            "emerg_budget": 40,
            "surg_budget": 40,
            "matern_budget": 20
            }
    return bud_areas

def print_msgs(p_budget_areas:dict):

    str_area_1 = str(p_budget_areas["emerg_budget"])
    str_area_2 = str(p_budget_areas["surg_budget"])
    str_area_3 = str(p_budget_areas["matern_budget"])


    # Out variables
    msg_1 = "\nPresupuestos anuales:"
    msg_2 = (f"- Total de presupuesto del área de Emergencias es del {str_area_1}% anual")
    msg_3 = (f"- Total de presupuesto del área de Cirugías es del {str_area_2}% anual")
    msg_4 = (f"- Total de presupuesto del área de Maternidad es del {str_area_3}% anual\n")

    msg_dict = {
        "msg1": msg_1,
        "msg2": msg_2,
        "msg3": msg_3,
        "msg4": msg_4
    }

    for values in msg_dict.values():
        print(values)