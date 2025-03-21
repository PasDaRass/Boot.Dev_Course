def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in items:
        if i == "Potion":
            potion_count += 1
        elif i == "Bread":
            bread_count += 1
        elif i == "Shortsword":
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count
