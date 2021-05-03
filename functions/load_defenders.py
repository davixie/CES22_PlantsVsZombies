from classes.defensor.export import Defensor

def load_defenders(defensor_group):
    defensor = Defensor(0, 300, 0, './assets/alcool_gel.png')
    defensor_group.add(defensor)