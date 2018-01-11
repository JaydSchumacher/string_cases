def stringcases(str):
    '''uppercase
    lowercase
    titlecased
    reverse'''

    str_up = str.upper()
    str_lower = str.lower()
    str_title = str.title()
    str_rev = ''
    for letter in reversed(str):
        str_rev = str_rev + letter

    return(str_up, str_lower, str_title, str_rev)

print(stringcases("Hello World"))