def validate_path(expected_path, character_path):
    character_name = character_path[0]
    waypoints = 0
    index = 0
    del character_path[0]
    
    for i in expected_path:
        for x in character_path:
            if i == x:
                waypoints += 1

    percentage = (waypoints / len(expected_path)) * 100
    return character_name, round(float(percentage))
