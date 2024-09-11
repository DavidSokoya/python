# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"
def name_shuffler(str_):
    new_str = str_.split(' ')
    
    first_name = new_str[0]
    last_name = new_str[1]
    
    return f"{last_name} {first_name}"

def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first

def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])