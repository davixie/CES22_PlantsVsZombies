from classes.defensor.defensor import Defensor
from classes.defensor.power.vacina import Vacina_Power
from assets.export import doctor_images_list

class Medico(Defensor):
    def __init__(self, position_x, position_y, defensor_power_group):
        list_image = doctor_images_list
        power = 4.0
        resistence = 0.8
        super().__init__(position_x, position_y, resistence, power, list_image, defensor_power_group)
        self.rect[0] = self.position_x
        self.rect[1] = self.position_y
        self.attack_frequency=60
    
    def atack(self, defensor_power_group):
        defensor_power = Vacina_Power(self.position_x, self.position_y, self.power)
        defensor_power_group.add(defensor_power)