def find_min(nums):
    min = float("inf")

    for i in nums:
        if i < min:
            min = i
    return min
