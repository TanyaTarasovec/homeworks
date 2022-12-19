def get_winners(results):
    sorted_results = sorted(results, reverse=True)
    res = []
    for index in range(3):
        points = sorted_results[index]
        win_num = results.index(points) + 1
        res.append(win_num)
    return res


print(get_winners([100, 352, 500, 600, 0]))
