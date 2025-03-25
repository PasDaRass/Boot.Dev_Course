def find_missing_ids(first_ids, second_ids):
    filter_id_set = set()
    for id in first_ids:
        if id not in second_ids:
            filter_id_set.add(id)
    return list(filter_id_set)
