X = input ('Give me a word and i gonna tell you if it is a palindrome: ')
Y = X

if Y == X[::-1]: print ('Is a palindrome')
else:
    print('Is not a palindrome')