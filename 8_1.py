class ConfigParser:

    def __init__(self, user_text):
        self.my_dict = {}
        self.text = user_text

    def string_to_dict(self):
        my_items = self.text.split('\n')
        my_key = ''
        for sect in my_items:
            if sect == '':
                continue
            if sect.startswith('[') and sect.endswith(']'):
                my_key = sect[1:-1]
                self.my_dict[my_key] = {}
            else:
                sect = sect.split('=')
                key, value = sect
                self.my_dict[my_key][key] = value
        return self.my_dict

    def get(self, sect, key):
        if sect not in self.my_dict:
            raise ValueError("Нет такого раздела.")
        elif key not in self.my_dict[sect]:
            raise ValueError("Нет такого ключа.")
        else:
            return self.my_dict[sect][key]

    def add_section(self, new_sect):
        if new_sect in self.my_dict:
            raise ValueError("Такой раздел уже есть.")
        else:
            self.my_dict[new_sect] = {}

    def add_param(self, sect, key, new_val):
        if sect not in self.my_dict:
            raise ValueError('Такой раздел отсутствует.')
        else:
            self.my_dict[sect][key] = new_val

    def has_section(self, sect):
        if sect in self.my_dict.keys():
            return True
        return False

    def has_param(self, sect, param_key):
        if sect in self.my_dict.keys():
            if param_key in self.my_dict[sect].keys():
                return True
            else:
                return False
        raise ValueError("Такой раздел отсутствует.")

    def del_section(self, sect):
        if sect in self.my_dict:
            del self.my_dict[sect]
        return self.my_dict

    def del_param(self, sect, param_key):
        if sect in self.my_dict:
            if param_key in self.my_dict[sect]:
                del self.my_dict[sect][param_key]
        return self.my_dict

    def __str__(self):
        temp_dict = []
        for sect, item in self.my_dict.items():
            temp_dict.append(f'[{sect}]')
            for key, val in item.items():
                temp_dict.append(f'{key} = {val}')
        return '\n'.join(temp_dict)


text = '''
[Section1]
key1=value1
key2=value2

[Section2]
key3=value3
key4=value4
key5=value5
'''

my_text = ConfigParser(text)
a = my_text.string_to_dict()
print(a)
print(my_text.get('Section2', 'key3'))
my_text.add_section('Section3')
my_text.add_param('Section3', 'key6', 'val6')
print(a)
print(my_text.has_section('Section4'))
print(my_text.has_param('Section2', 'key4'))
print(my_text.del_section('Section1'))
print(my_text.del_param('Section2', 'key4'))
print(my_text)
