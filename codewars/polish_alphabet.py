# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

# Your task is to change the letters with diacritics:

# ą -> a,
# ć -> c,
# ę -> e,
# ł -> l,
# ń -> n,
# ó -> o,
# ś -> s,
# ź -> z,
# ż -> z
# and print out the string without the use of the Polish letters.

polish_to_latin = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
    }

def correct_polish_letters(st): 
    result = ''
    for char in st:
        if char in polish_to_latin:
            result += polish_to_latin[char]
        else: 
            result += char
    return result
   