from point import Point
from matrix import Matrix


def main():
    rows = input("Enter number of rows: ")
    cols = input("Enter number of cols: ")
    m = Matrix(rows, cols)
    start_weight = m.sum_of_weight()
    max_damage = 0
    points_damage = {}
    for point in m.full:
        damage = start_weight - damage_of(point, m)
        if damage >= max_damage:
            max_damage = damage
        points_damage[point] = damage 
    print(points_damage)


def damage_of(p, m):
    d = 0
    negh = p.neighbours(m)
    for n in negh:
        diff = n - p
        if diff > 0:
            d += p.weight
        else:
            d += n.weight
    return d

if __name__ == '__main__':
    main()
