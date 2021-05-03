from classes.defensor.export import Defensor
from constants import rows

def load_defenders(defensor_group):
    defensor = Defensor(0, rows[0], 0, './assets/defensor/medico.png')
    defensor_group.add(defensor)