my_dct = {'id0': {'f_name': 'Alex', 'l_name': 'Smith', 'phone': '1234567890', 'mail': 'alsm@google.com'},
          'id1': {'f_name': 'Bart', 'l_name': 'Jonson', 'phone': '1234567890', 'mail': ''},
          'id2': {'f_name': 'Carl', 'l_name': 'Beninghton', 'phone': '1234567890'}
          }

for id, data in my_dct.items():
    if not data.get('mail'):
        print(data['f_name'])
