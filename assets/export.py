import pygame
import os

SQUARE_X = 82
SQUARE_Y = 130

SQUARE_POWER_X = 35
SQUARE_POWER_Y = 48

first_attacker_1 = pygame.image.load(os.path.join('assets','artes finais','atacantes','virus1_1.png'))
first_attacker_1 = pygame.transform.scale(first_attacker_1, (SQUARE_X, SQUARE_Y))
first_attacker_2 = pygame.image.load(os.path.join('assets','artes finais','atacantes','virus1_2.png'))
first_attacker_2 = pygame.transform.scale(first_attacker_2, (SQUARE_X, SQUARE_Y))
first_attacker_images_list = [first_attacker_1, first_attacker_2]

second_attacker_2 = pygame.image.load(os.path.join('assets','artes finais','atacantes','sick.png'))
second_attacker_2 = pygame.transform.scale(second_attacker_2, (SQUARE_X, SQUARE_Y))
second_attacker_images_list = [second_attacker_2]

doctor_1 = pygame.image.load(os.path.join('assets','artes finais','defensor 1','doctor_1.png'))
doctor_1 = pygame.transform.scale(doctor_1, (SQUARE_X, SQUARE_Y))
doctor_2 = pygame.image.load(os.path.join('assets','artes finais','defensor 1','doctor_2.png'))
doctor_2 = pygame.transform.scale(doctor_2, (SQUARE_X, SQUARE_Y))
doctor_power = pygame.image.load(os.path.join('assets','artes finais','defensor 1','doctor_item.png'))
doctor_power = pygame.transform.scale(doctor_power, (SQUARE_POWER_X, SQUARE_POWER_Y))
doctor_images_list = [doctor_1, doctor_2]
doctor_power_images_list = [doctor_power]

nurse_1 = pygame.image.load(os.path.join('assets','artes finais','defensor 2','nurse_1.png'))
nurse_1 = pygame.transform.scale(nurse_1, (SQUARE_X, SQUARE_Y))
nurse_2 = pygame.image.load(os.path.join('assets','artes finais','defensor 2','nurse_2.png'))
nurse_2 = pygame.transform.scale(nurse_2, (SQUARE_X, SQUARE_Y))
nurse_power = pygame.image.load(os.path.join('assets','artes finais','defensor 2','nurse_item.png'))
nurse_power = pygame.transform.scale(nurse_power, (SQUARE_POWER_X, SQUARE_POWER_Y))
nurse_images_list = [nurse_1, nurse_2]
nurse_power_images_list = [nurse_power]

alcohol_1 = pygame.image.load(os.path.join('assets','artes finais','defensor 3','alcohol_1.png'))
alcohol_1 = pygame.transform.scale(alcohol_1, (SQUARE_X, SQUARE_Y))
alcohol_2 = pygame.image.load(os.path.join('assets','artes finais','defensor 3','alcohol_2.png'))
alcohol_2 = pygame.transform.scale(alcohol_2, (SQUARE_X, SQUARE_Y))
alcohol_power = pygame.image.load(os.path.join('assets','artes finais','defensor 3','alcohol_item.png'))
alcohol_power = pygame.transform.scale(alcohol_power, (SQUARE_POWER_X, SQUARE_POWER_Y))
alcohol_images_list = [alcohol_1, alcohol_2]
alcohol_power_images_list = [alcohol_power]

mask = pygame.image.load(os.path.join('assets','artes finais','defensor 4','mask.png'))
mask = pygame.transform.scale(mask, (SQUARE_X, SQUARE_Y))
mask_images_list = [mask]

scientist_1 = pygame.image.load(os.path.join('assets','artes finais','defensor 5','scientist_1.png'))
scientist_1 = pygame.transform.scale(scientist_1, (SQUARE_X, SQUARE_Y))
scientist_2 = pygame.image.load(os.path.join('assets','artes finais','defensor 5','scientist_2.png'))
scientist_2 = pygame.transform.scale(scientist_2, (SQUARE_X, SQUARE_Y))
scientist_power = pygame.image.load(os.path.join('assets','artes finais','defensor 5','scientist_item.png'))
scientist_power = pygame.transform.scale(scientist_power, (SQUARE_POWER_X, SQUARE_POWER_Y))
scientist_images_list = [scientist_1, scientist_2]
scientist_power_images_list = [scientist_power]

final_defensor_image = os.path.join('assets','artes finais','defensor 3','alcohol.png')