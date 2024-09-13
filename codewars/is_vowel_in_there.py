# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

# If they are, change the array value to a string of that vowel.

# Return the resulting array.



def is_vow(numbers):

    vowel_codes = {
      97: 'a',
      101: 'e',
      105: 'i',
      111: 'o',
      117: 'u'
        }

    result = []
    for num in numbers:
        if num in vowel_codes:
             result.append(vowel_codes[num])
        else:
             result.append(num)
    return result