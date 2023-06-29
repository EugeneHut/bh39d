city = input('Enter city: ')
my_dct = {'Belarus': ['Minsk', 'Brest', 'Hrodno'], 'Poland': ['Warsaw', 'Gdansk', 'Belostoc'],
          'Germany': ['Berlin', 'Drezden', 'Munich']}
for key, value in my_dct.items():
    if city in value:
        print(key)
