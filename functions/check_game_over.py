def check_game_over(atacante_group):
    for atacante in atacante_group:
        if atacante.positionx < 150:
            return True