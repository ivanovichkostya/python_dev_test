planets = {
	'Меркурий': 57910006,
	'Венера': 108199995,
	'Земля': 57910006,
	'Марс': 108199995,
    'Юпитер': 108199995,
	'Сатурн': 57910006,
	'Уран': 108199995,
    'Нептун': 4504299579.
}
average_distance_to_sun = sum(list(planets.values())) / len(planets)
sorted_list_of_planets = sorted(list(planets.keys()))
distance = planets['Нептун'] / planets['Земля']

print('Среднее расстояние до солнца: ', average_distance_to_sun)
print( 'Список плает: ' , sorted_list_of_planets)
print( 'Насколько Нептун дальше от Солнца : ' , distance)