from classes.defensor.defensor import Defensor
from classes.defensor.power.scientist_power import Scientist_Power
from assets.export import scientist_images_list

class Cientista(Defensor):
    def __init__(self, position_x, position_y, defensor_power_group):
        list_image = scientist_images_list
        power = 0.8
        resistence = 0.8
        super().__init__(position_x, position_y, resistence, power, list_image, defensor_power_group)
        self.rect[0] = self.position_x
        self.rect[1] = self.position_y

    def atack(self, defensor_power_group):
        defensor_power = Scientist_Power(self.position_x, self.position_y, self.power)
        defensor_power_group.add(defensor_power)
