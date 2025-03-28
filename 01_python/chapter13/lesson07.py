def divide_list(nums, divisor):
    divided = []

    for i in nums:
        divided.append(round(i / divisor, 2))
    return divided
