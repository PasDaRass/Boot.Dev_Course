def area_sum(rectangles):
    result = 0
    for i in rectangles:
        result += (i["height"] * i["width"])
    return result
