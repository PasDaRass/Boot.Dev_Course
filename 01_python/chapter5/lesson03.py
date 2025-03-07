def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    total_damage -= resist
    return health - total_damage
