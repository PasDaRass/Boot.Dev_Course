def calculate_flurry_crit(num_attacks, base_damage):
        total_damage = 0
        if num_attacks != 0:
            for i in range(0, num_attacks):
                total_damage += (base_damage * 2)
            total_damage += (base_damage * 2)
        return total_damage
