def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line
    unpurchased_items = []
    receipt = {}
    total_cost = 0.0

    for i in pinned_list:
        if i not in items_purchased:
            unpurchased_items.append(i)
    for i in items_purchased:
        if i in item_prices:
            receipt[i] = item_prices[i]
    for k in receipt:
        total_cost += receipt[k]
        
    return unpurchased_items, receipt, total_cost
