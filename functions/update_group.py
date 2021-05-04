def update_groups(groups, screen):
    for group in groups:
        update_group(group, screen)

def update_group(group, screen):
    group.update()
    group.draw(screen)