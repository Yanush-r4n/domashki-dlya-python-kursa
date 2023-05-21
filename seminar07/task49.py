def find_farthest_orbit(list_of_orbits):
    temp = list(map(lambda x: x[0] * x[1] if x[0] != x[1] else 0, orbits))
    max_temp = max(temp)
    temp = temp.index(max_temp)

    return list_of_orbits[temp]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(orbits)
print(find_farthest_orbit(orbits))