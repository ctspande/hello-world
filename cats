print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats a lot of cats')
    if int(numCats) < 0:
        print('You cannot have negative cats')
    else:
        print('That is not a lot of cats')
except ValueError:
    print('you did not enter a number')
