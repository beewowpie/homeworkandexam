
# 8.Есть словарь песен группы Depeche Mode
# violator songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56,
#                        'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
#                        'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова

violator_songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56,
                       'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
                     'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }

z = list(violator_songsdict.values())
s = sum(z)
print('Общее время звучания альбома: ',s,'минут')

v_s = {key: float(values) for key, values in violator_songsdict.items() if float(values) > 5.00}
print('Список песен, продолжительностью более 5 минут: ',list(v_s))

v_s1 = {key: float(values) for key, values in violator_songsdict.items() if ' ' not in key}
print('Словарь из песен, название которых состоит из одного слова: ',v_s1)

