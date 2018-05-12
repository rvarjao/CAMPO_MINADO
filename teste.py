#
# initial = 10000
# offset = 2000
# final = initial + offset
#
# for i in range(initial, final):
#     print("char({}) : {}".format(i, chr(i)))

from CAMPO_MINADO import Point

points = [Point(1,2), Point(3,2), Point(5,5)]

for (i, point) in enumerate(points):
    print(i,point)