print("Guess a number between 1 and 1000 and I will try to guess it")
    

def guess_number(previous_number):
    max_number = 1000
    min_number = 1
    current_number = 0
    keepgoing = True
    while keepgoing:
        guess = input('My guess is ' + str(previous_number) + ' Enter H for higher, L for Lower, or C if this is your number ')
        previous_number = int(previous_number)
        if guess.lower() == 'h':
            min_number = previous_number
            previous_number = round((previous_number + max_number) / 2)
        elif guess.lower() == 'l':
            max_number = previous_number
            previous_number = round((previous_number + min_number) /2)
        elif guess.lower()  == 'c':
            keepgoing = False
            return "Im just that good"
        else:
            print("Invalid entry, make sure you use H, L, or C.")
        
        
        
        


print(guess_number(500))
