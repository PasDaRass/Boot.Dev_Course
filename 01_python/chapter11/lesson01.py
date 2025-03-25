def remove_duplicates(spells):
    spells_set = set(spells)
    list_spells = list(spells_set) 
    return list_spells
    
"""    
def remove_duplicates(spells):
    spells_set = set()
    list_spells = []

    for spell in spells:
        spells_set.add(spell)
        if spell not in list_spells:
            list_spells.append(spell)
    return list_spells
"""          
