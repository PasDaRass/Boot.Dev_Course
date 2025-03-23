def get_most_common_enemy(enemies_dict):
    enemy_name = None
    high_count = float("-inf")
    
    for enemy in enemies_dict:
        if enemies_dict[enemy] > high_count:
            enemy_name = enemy
            high_count = enemies_dict[enemy]
    print(enemy_name, high_count)
    return enemy_name
