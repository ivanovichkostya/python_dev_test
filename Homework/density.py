density = [8.56, 3.5, 139, 32, 23.6, 2.8, 357]
average_density = sum(density) / len(density)

print(average_density)

density = [8.56, 3.5, 139, 32, 23.6, 2.8, 357]
density_sort = sorted(density)
minimum_density = density_sort[0]

print(minimum_density)


density = [8.56, 3.5, 139, 32, 23.6, 2.8, 357]
density_sort = sorted(density)
maximum_density = density_sort[len(density) -1]

print(maximum_density)



density = [8.56, 3.5, 139, 32, 23.6, 2.8, 357]
density_sort = sorted(density)
biggest_numbers_density=density_sort[len(density) -3:]

print(biggest_numbers_density)