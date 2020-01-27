given_string = input('Enter a number or string to find out how many characters it has ')

def str_count(string):
    if not string:
        return 0
    else:
        return 1 + str_count(string[:-1])
        
print(str_count(given_string))