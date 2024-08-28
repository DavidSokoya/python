# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    newStr = ''
    for i in s:
        if i == '!':
            newStr += ''
        else:
            newStr += i