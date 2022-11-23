point_x1 = int(input("Введите координату x1:"))
print(point_x1)

point_y1 = int(input("Введите координату y1:"))
print(point_y1)

point_x2 = int(input("Введите координату x2:"))
print(point_x2)

point_y2 = int(input("Введите координату y2:"))
print(point_y2)

distance_of_points = ((point_x1 - point_y1)**2 + (point_x2 - point_y2)**2)**2
print(f"Расстояние между точками: {distance_of_points}")
