from classes.defensor.final_defense import FinalDefensor
from assets.export import final_defensor_image
from constants import SCREEN_WIDTH, rows

def load_final_defenses(final_defensor_group):
    final_defensor_1 = FinalDefensor(350, 120, 0, final_defensor_image)
    final_defensor_2 = FinalDefensor(350, 260, 0, final_defensor_image)
    final_defensor_3 = FinalDefensor(350, 400, 0, final_defensor_image)
    final_defensor_4 = FinalDefensor(350, 540, 0, final_defensor_image)
    final_defensor_5 = FinalDefensor(350, 680, 0, final_defensor_image)
    final_defensor_group.add(final_defensor_1)
    final_defensor_group.add(final_defensor_2)
    final_defensor_group.add(final_defensor_3)
    final_defensor_group.add(final_defensor_4)
    final_defensor_group.add(final_defensor_5)
    