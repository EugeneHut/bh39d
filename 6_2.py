my_text = input("Input text: ")


def translate_to_morse(text):
    text = text.upper()
    morse_text = ''
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'J': '.---',
        'I': '..', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    } 
    for i in text:
        if i != morse_code_dict.keys():
            morse_text += ' '
        for key, value in morse_code_dict.items():
            if i == key:
                morse_text += value
    return morse_text


print(translate_to_morse(my_text))
