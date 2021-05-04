from classes.defensor.defensor import Defensor
from classes.defensor.power.alcool_gel import Alcool_Gel_Power
from assets.export import alcohol_images_list

class Alcool_E_Gel(Defensor):
    def __init__(self, position_x, position_y, defensor_power_group):
        list_image = alcohol_images_list
        resistence = 0.8
        power = 0.8
        super().__init__(position_x, position_y, resistence, power, list_image, defensor_power_group)
        # self.rect.center = (self.position_x, self.position_y)
        self.rect[0] = self.position_x
        self.rect[1] = self.position_y
    
    def atack(self, defensor_power_group):
        # load_alcool_gel_power(position_x, position_y, defensor_power_group)
        defensor_power = Alcool_Gel_Power(self.position_x, self.position_y, self.power)
        defensor_power_group.add(defensor_power)