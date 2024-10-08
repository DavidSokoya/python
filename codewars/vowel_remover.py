# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"

def shortcut( s ):
    vowel = 'aeiou'
    
    res = ''
    for letter in s:
        if letter in vowel:
            res += ''
        else:
            res += letter
    return res