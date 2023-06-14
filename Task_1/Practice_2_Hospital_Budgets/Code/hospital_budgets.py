
from hb_functions import *

print("\nBienvenidos")
print("\nHospital Matasanos")
print("Sistema de presupuestos")

# Birth type variables
natural_births = 0
cesarean_births = 0

natural_births = get_nbs_data()
cesarean_births = get_cbs_data()

budget_areas = validate_births(natural_births, cesarean_births)

print_msgs(budget_areas)