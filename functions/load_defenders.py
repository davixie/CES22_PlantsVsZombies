from classes.defensor.export import Defensor

def load_defenders(defensor_group):
    defensor = Defensor(0, 300, 0, './assets/defensor/medico.png')
    defensor_group.add(defensor)