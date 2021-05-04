from classes.defensor.export import Alcool_E_Gel, Medico, Mascara, Enfermeiro
from constants import rows

def load_defenders(defensor_group, defensor_power_group):
    defensor = Alcool_E_Gel(0, rows[0], defensor_power_group)
    medico = Medico(0 , rows[1], defensor_power_group)
    mascara = Mascara(0, rows[2], defensor_power_group)
    enfermeiro = Enfermeiro(0, rows[3], defensor_power_group)
    defensor_group.add(defensor)
    defensor_group.add(medico)
    defensor_group.add(mascara)
    defensor_group.add(enfermeiro)