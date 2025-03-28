def remove_nonints(nums):
    filtered = []
    for i in nums:
        if type(i) == int:
            filtered.append(i)
    return filtered
