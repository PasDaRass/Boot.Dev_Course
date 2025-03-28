def join_strings(strings):
    joined = ""
    for s in strings:
        joined += s + ","
    if len(joined) != 0:
        joined = joined[:-1]
    return joined
