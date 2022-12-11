def distance(*args):
    summ_distance = 0
    for index, coords in enumerate(args):
        if index == len(args) - 1:
            break
        x1, y1 = coords
        x2, y2 = args[index+1]
        line = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        summ_distance += line
    return summ_distance


result = distance((1, 1), (1, 2), (2, 2))
print(result)
